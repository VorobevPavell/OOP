class Cat():

    __shared_attr = {
        'breed' : 'pers',
        'color' : 'black'
    }

    def __init__(self) -> None:
        self.__dict__ = self.__shared_attr


Tom = Cat()
Jerry = Cat()
print(Tom.breed)
print(Jerry.breed)
Tom.breed = 'siam'
print(Tom.breed)
print(Jerry.breed)
Tom.name = 'tommy'
print(Tom.name)
print(Jerry.name)
