""" Создайте класс Lion. В нем должен быть метод roar,который печатает на экран "Rrrrrrr!!!"
Пример работы с классом Lion :
simba = Lion()
simba.roar() # печатает Rrrrrrr!!! """


class Lion():
    def roar(self):
        return "Rrrrrrr!!!"

simba = Lion()
print(simba.roar())