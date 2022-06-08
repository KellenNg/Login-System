import hashlib

from Auth import Auth


class Login(Auth):
    def get_credentials(self):
        return True

    def validation(self):
        number = 0
        with open("credentials.txt", mode="r", encoding="UTF-8") as file:
            for line in file:
                line = line.strip()
                list = line.split(",")
                if list[0].strip() == self.username:
                    m = hashlib.md5()
                    data = self.password.encode('utf-8')
                    m.update(data)
                    hashed = m.hexdigest()
                    if hashed == list[1].strip():
                        number += 1
                    else:
                        password_again = input("Please enter your credentials again: ")
                        m = hashlib.md5()
                        data_again = password_again.encode('utf-8')
                        m.update(data_again)
                        hashed_again = m.hexdigest()
                        if hashed_again == list[1].strip():
                            number += 1
                        else:
                            number = number
                else:
                    number = number
            if number != 0:
                print("Successful Login")
            else:
                print("Not successful Login")
