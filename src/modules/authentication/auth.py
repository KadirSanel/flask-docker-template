# example class
class Auth:

    def __init__(self):
        self.is_auth = False

    def set_is_auth(self, is_auth):
        self.is_auth = is_auth

    def get_is_auth(self):
        return self.is_auth