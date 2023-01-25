class Car():
    model = 'BMW'
    engine = 1.6

a = Car()
b = Car()
print(a.model)
print(b.engine)
print('___________')
b.seat = 4
print(a.__dict__)
print(b.__dict__)
print('___________')
a.model = "Lada"
print(a.__dict__)
print(a.model)
print('___________')
del a.model
print(a.model)