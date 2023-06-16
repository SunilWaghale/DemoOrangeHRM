import configparser

config = configparser.RawConfigParser()

config.read("D:\\A A Python Practices Project\\Tushar Sir Python Selenium\\OrangeHRM 15 jun 23\\OrangeHRMNew\\Configuration\\config.ini")


class ReadValue():

    @staticmethod
    def getUsername():
        username = config.get('login info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('login info', 'password')
        return password
    @staticmethod
    def getUrl():
        url = config.get('login info', 'Url')
        return url

# noncommerce
# php travel
# lorri
# IRCTC
# https://automation.credence.in/shop