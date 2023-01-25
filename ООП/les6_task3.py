class Zebra():
    def __init__(self,count=0) -> None:
        self.count=count
    def which_strip(self):
        if self.count % 2 == 0 :
            print('white')
            self.count += 1
        else:
            print('black')
            self.count += 1



z1 = Zebra()
z1.which_strip()
z1.which_strip()
z1.which_strip()
print('________')
z2 = Zebra()
z2.which_strip()
print('________')
z3 = Zebra()
z3.which_strip()

