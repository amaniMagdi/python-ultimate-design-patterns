class User:
    def __init__(self, email: str, mobile: str):
        self._email = email
        self._mobile = mobile

    @property
    def email(self) -> str:
        return self._email
    
    @property
    def mobile(self) -> str:
        return self._mobile
    
    @email.setter
    def email(self, value) -> None:
        self._email = value

    @mobile.setter
    def mobile(self, value) -> None:
        self._mobile = value