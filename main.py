from Registration import Registration
from Login import Login


class Main(Registration, Login):
        print("If you want to registrate, please write 1; if you want to login in, please write 2")
        number_choise = int(input("Which number would you want to choose: "))
        while number_choise == 1:
            Kellen = Registration(input("Registrate your username: "), input("Registrate your password: "))
            Kellen.store_data(Kellen.get_credentials())
            print("If you want to login in, please write 1; if you want to registrate, please write 2")
            number_choise = int(input("Which number would you want to choose: "))
        if number_choise == 2:
            Kellen = Login(input("Please enter your username: "), input("Please enter your credentials: "))
            Kellen.validation()
        else:  # data verification
            print("Are you blind? You must choose 1 or 2!")
