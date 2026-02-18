from bcrypt import hashpw, checkpw, gensalt


def get_hash(password: str):
    password = password.encode()
    hashed = hashpw(password, gensalt())
    return hashed


def verify(password: str, hashed: str):
    password = password.encode()
    hashed = hashed.encode()
    return checkpw(password, hashed)
