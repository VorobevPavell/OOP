class Cat():
    def __init__(self,name,color='red',breed='pers',age=10) -> None:
        self.color = color
        self.name = name
        self.age = age
        self.breed = breed
        print(f'hello {name,color,breed,age}' )

tom = Cat('TOM','black','siam',0)