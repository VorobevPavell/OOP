class Car():
    model = 'BMW'
    engine = 1.6

    @staticmethod
    def drive():
        return 'Let\'s go !'
print(Car.__dict__)
print(Car.drive())
print(getattr(Car,'drive')())
a = Car()
print(a.drive())