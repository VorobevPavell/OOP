class PizzaMaker():

    def __make_pepperoni(self):
        print('pepp')
    def __make_bbq(self):
        print('bbq')

maker = PizzaMaker()
#print(PizzaMaker.__dict__.keys())
print(maker._PizzaMaker__make_bbq())
print(maker._PizzaMaker__make_pepperoni())