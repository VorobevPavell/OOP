class Cat():
    breed = 'pers'
    def hello(*args):
        return 'Hello world from kitty',args
    def show_breed(self):
        return f'my breed is {self.breed} '
    def show_name(self):
        if hasattr(self,'name'):
            return f'my name is {self.name}'
        else:
            return 'noname'
    def set_value(self,value,age = 0):
        self.name = value
        return value,f'age is {age}'

a = Cat()
print(a.hello())
print(a)
print('___________')
b = Cat()
print(b.hello())
print(b)
print('_________')
walt = Cat()
print(walt.show_breed())
walt.breed = 'siam'
print(walt.show_breed())
bob = Cat()
print(bob.show_breed())
mary = Cat()
mary.name = "MARY"
print(mary.show_name())
print(bob.show_name())
bars = Cat()
print(bars.show_name())
print(bars.set_value('BARSIK',12))
print(bars.show_name())