from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Header

from sqlalchemy.orm import Session

from .database import Base
from .database import engine
from .database import get_db

from .models import User
from .models import Preference

from .schemas import RegisterRequest
from .schemas import LoginRequest
from .schemas import PreferenceRequest

from .auth import hash_password
from .auth import verify_password
from .auth import create_access_token
from .auth import decode_token

from .news import fetch_news

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Personalized News Aggregator API",
    description="""
    REST API for:
    - User Registration
    - JWT Authentication
    - User Preferences
    - Personalized News Feed
    - News Search
    """,
    version="1.0.0",
    contact={
        "name": "Anwar Shaik",
        "email": "anwar160161@gmail.com"
    }
)
security = HTTPBearer()

def get_current_user(token: str):
    try:
        payload = decode_token(token)
        return payload["user_id"]
    except:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )


@app.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):

    existing = db.query(User).filter(
        User.email == request.email
    ).first()

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    user = User(
        username=request.username,
        email=request.email,
        password=hash_password(request.password)
    )

    db.add(user)
    db.commit()

    return {
        "message": "User registered"
    }


@app.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    user = db.query(User).filter(
        User.email == request.email
    ).first()

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    if not verify_password(
        request.password,
        user.password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )

    token = create_access_token(
        {"user_id": user.id}
    )

    return {"access_token": token}


@app.put("/preferences")
def save_preferences(
    request: PreferenceRequest,
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    user_id = get_current_user(token)

    db.query(Preference).filter(
        Preference.user_id == user_id
    ).delete()

    for category in request.categories:
        db.add(
            Preference(
                category=category,
                user_id=user_id
            )
        )

    db.commit()

    return {
        "message": "Preferences saved"
    }

@app.get("/news")
def get_news(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):

    token = credentials.credentials

    user_id = get_current_user(token)

    prefs = db.query(Preference).filter(
        Preference.user_id == user_id
    ).all()

    articles = []

    for pref in prefs:
        articles.extend(
            fetch_news(pref.category)
        )

    return articles[:20]

@app.get("/news/search")
def search_news(q: str):
    return fetch_news(q)