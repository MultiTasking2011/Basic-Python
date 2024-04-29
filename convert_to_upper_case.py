def CTUC(func):
    def wrapper():
        a = func()
        return a.upper()       
    return wrapper