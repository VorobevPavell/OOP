class Person: # создаю класс Person с атрибутами имя и возраст
    name = "Pavel"
    age = 19


print(Person.name) # обращаюсь к атрибутам созданного класса
print(Person.age)
print('-----------')
c = Person() # создам объект (экземпляр) класса Person
print(c)
print("------------")
print('команда __dict__ позволяет узнать атрибуты класса')
print(Person.__dict__)
print("------------")
print(getattr(Person,'age'),getattr(Person,'name'),getattr(Person,'X','Вернется если нет атрибута X'))
print("------------")
Person.age = 20
Person.name = "Nastya"
Person.x = 'New atrribute'
print(Person.__dict__)
print("------------")
print(Person.x)
print("Команда setattr позволяет изменять атрибуты или создавать новые")
setattr(Person,'is_fake',False)
print(Person.__dict__)
print("------------")
print(Person.is_fake)

a = Person() # экземпляр класса
b = Person()
a.last_name = 'Vorobev'
b.l_n = 'Shep'
print(a.__dict__)
print(b.__dict__)