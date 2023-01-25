class Student():

    def __init__(self,name,age,branch) -> None:
        self.__name = name
        self.__age = age
        self.__branch = branch
    
    def __display_details(self):
        print('Имя: ',self.__name)
        print('Возраст: ',self.__age)
        print('Направление: ',self.__branch)

    def access_private_method(self):
        self.__display_details()


obj = Student('Adam Smith',25,'Inforamion Technology')
obj.access_private_method()

#Output
""" Имя:  Adam Smith
Возраст:  25
Направление:  Inforamion Technology """