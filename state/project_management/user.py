class User:
    def __init__(self, email):
        self.__email = email

    @property
    def email(self):
        return self.__email
    