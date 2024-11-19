class Person:
    def __init__(self, name,email):
        self.__name = name
        self.__email = email

    def getter(self):
        return self.__name, self.__email
    
    def setter(self,ad,eposta):
        self.__name = ad
        self.__email = eposta
        return self.__name , self.__email
    
    @property
    def introduce(self):
        return "Name : {}, Email : {}".format(self.__name,self.__email)
    