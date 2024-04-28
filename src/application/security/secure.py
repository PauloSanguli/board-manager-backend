"""has password and check password methods"""

import bcrypt



class PasswordSecure:
    def encrypt(password: str) -> str:
        """encrypt password and returnning"""

        salt = bcrypt.gensalt()

        password_hashed = bcrypt.hashpw(password.encode('utf-8'), salt)

        return password_hashed
    
    def check(password: str, password_hash: str) -> bool:
        """verifty if the password inserted inserted stay in db"""

        __result = bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8'))

        return __result
