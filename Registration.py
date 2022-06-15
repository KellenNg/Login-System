import hashlib

from Auth import Auth


class Registration(Auth):
    def validate_username(self):
        if self.get_data():
            return False
        return True

    def validate_password(self):
        if len(self.password) >= 8:
            return True
        return False

    def get_credentials(self):
        if self.validate_username():
            print("The username can be used")
            while not self.validate_password():
                print("The password should equal or more than 8 characters.")
                self.password = input("Registrate your password: ")
            else:
                if self.password == input("Enter your password again: "):
                    print("The password can be used")
                    m = hashlib.md5()
                    data = self.password.encode('utf-8')
                    m.update(data)
                    hashed = m.hexdigest()
                    return hashed
                else:
                    print("The password is different from the password at first")
        else:
            print("Please enter different username, this username has been used!")
            