class Auth:
    # constructor(構造函數)
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def store_data(self, password):
        file = open("credentials.txt", "a")
        if password:
            file.write("\n" + self.username + ", " + password)  # concatenation(串聯)
            file.close()
        else:
            file.close()

    def get_data(self):
        with open("credentials.txt", mode="r", encoding="UTF-8") as file:
            for line in file:
                line = line.strip()  # remove前面的空格(string),如果是list的key，value就是remove所有空格
                list = line.split(",")  # 從有","的地方開始分隔並去除","
                if list[0].strip() == self.username:
                    return list[1].strip()
            return None
