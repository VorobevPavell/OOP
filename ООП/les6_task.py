class Laptop():

    def __init__(self,brand,model,price) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.laptop_name = f'{self.brand} {self.model}'
        return

hp = Laptop('hp','15-bw0xx',57000)
print(hp.price)
print(hp.laptop_name)

laptop1 = Laptop('apple','pro 13',100000)
laptop2 = Laptop('acer','2F-28fs',68000)
print(laptop1.model)