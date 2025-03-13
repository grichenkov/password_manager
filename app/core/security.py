import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SECRET_KEY = os.getenv("SECRET_KEY")

if not SECRET_KEY:
    raise ValueError("SECRET_KEY не найден в переменных окружения!")

cipher = Fernet(SECRET_KEY.encode())


def encrypt_password(password: str) -> str:
    """Шифрует пароль."""
    return cipher.encrypt(password.encode()).decode()


def decrypt_password(encrypted_password: str) -> str:
    """Расшифровывает пароль."""
    return cipher.decrypt(encrypted_password.encode()).decode()
