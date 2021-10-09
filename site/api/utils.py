from django.conf import settings
from random import choices
import datetime
import string
import bcrypt
import jwt


def create_password(val: str) -> str:
    hash = bcrypt.hashpw(val.encode('utf-8'), bcrypt.gensalt())
    return hash


def create_random_password(length: int = 10) -> str:
    symbols = "!#$*+-?_"
    symbols += string.ascii_letters
    symbols += string.digits

    if length < 1:
        length = 1

    if len(symbols) < length:
        while len(symbols) < length:
            symbols += symbols

    return ''.join(choices(list(symbols), k=length))


def check_password(hash: str, password: str) -> bool:
    return bcrypt.hashpw(password.encode('utf-8'), hash.encode('utf-8')) == hash.encode('utf-8')


def get_pairs_token(user: dict) -> tuple:
    sym = create_random_password()
    user['sym'] = sym

    t = datetime.datetime.utcnow()
    t += datetime.timedelta(days=1)

    user['exp'] = t.timestamp()

    token = jwt.encode(user, settings.JWT_KEY, algorithm="HS256")
    key = create_password(f"{user['id']}|{sym}|{user['is_admin']}").decode()

    return token, key