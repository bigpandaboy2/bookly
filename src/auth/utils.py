from passlib.context import CryptContext

passwd_context = CryptContext(schemes=["bcrypt"])

def generate_password_hash(password: str) -> str:
    hash = passwd_context.hash(password)

    return hash

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return passwd_context.verify(plain_password, hashed_password)