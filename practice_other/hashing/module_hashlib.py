import hashlib

def to_password(pas):
    return hashlib.sha512(pas)

def pasword_check():
    pass




if __name__ == '__main__':
    print(to_password(42))