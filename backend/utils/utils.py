from passlib.context import CryptContext
import hashlib
import hmac
from dotenv import load_dotenv
import os
load_dotenv()


SECRET_KEY = os.getenv('SECRET_KEY')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(psw: str):
    password_bytes = psw.encode('utf-8')
    key_bytes = SECRET_KEY.encode('utf-8')

    hash_object = hmac.new(key_bytes, password_bytes, hashlib.sha256)
    hash_hex = hash_object.hexdigest()
    return hash_hex

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return get_password_hash(plain_password) == hashed_password