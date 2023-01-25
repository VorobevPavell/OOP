""" Необходимо создать класс с именем Cat , создать внутри него 2 аттрибута name со значением Матроскин и color со значением 'black'. После этого создать экземпляр класса и сохранить его в переменную my_cat """

class Cat:
    name = 'Матроскин'
    color = 'black'

my_cat = Cat()
my_cat_2 = Cat()
my_cat_2.color = 'red'
print(my_cat.color)
print(my_cat_2.color)
