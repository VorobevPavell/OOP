# Инкапсуляция
class BankAccount():

    def __init__(self,name,balance,passport) -> None:
        self.__name = name
        self.__balance = balance
        self.__passport = passport

    def show_data(self):
        self.__show_private_data()
    #def show_protected_data(self):
     #   print(self._name,self._balance,self._passport)
    def __show_private_data(self):
        print(self.__name,self.__balance,self.__passport)


acccount1 = BankAccount('Bob',1000000,262384)
#acccount1.show_data()
print(acccount1._BankAccount__balance)
""" print(acccount1.__name)
print(acccount1.__balance)
print(acccount1.__passport) """