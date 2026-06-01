import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

SECRET_KEY = "mysecretkey"

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(password, hashed):
    return pwd_context.verify(password, hashed)


def create_access_token(data):
    payload = data.copy()

    payload["exp"] = (
        datetime.utcnow() + timedelta(hours=24)
    )

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm="HS256"
    )


def decode_token(token):
    return jwt.decode(
        token,
        SECRET_KEY,
        algorithms=["HS256"]
    )