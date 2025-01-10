class User:
    __username=None
    __password=None

    def __init__(self, username, password):
        self.__username=username
        self.__password=password

def main():
    user=User()
    