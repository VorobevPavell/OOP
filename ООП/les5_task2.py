""" Создайте класс Counter, экземпляры которого будут подсчитывать внутри себя значения.
В классе Counter нужно определить метод start_from, который принимает один необязательный аргумент - значение, с которого начинается подсчет. По умолчанию = 0
Также нужно создать метод increment, который увеличивает счетчик на 1.
Затем необходимо создать метод display, который печатает фразу "Текущее значение счетчика = <value>" и метод reset, который обнуляет экземпляр счетчика """

class Counter():
    value = 0
    def start_from(self,start=0):
        Counter.value = start
        return ''
    def increment(self):
        Counter.value += 1
        return ''
    def display(self):
        print(f"Текущее значение счетчика = {self.value}")
        return ''
    def reset(self):
        Counter.value = 0
        return ''

c1 = Counter()
c1.start_from()
c1.increment()
c1.display()
c1.increment()
c1.display()
c1.reset()
c1.display()
print('------')
c2 = Counter()
c2.start_from(3)
c2.display()
c2.increment()
c2.display()

"""
 results :
 Текущее значение счетчика = 1
Текущее значение счетчика = 2
Текущее значение счетчика = 0
------
Текущее значение счетчика = 3
Текущее значение счетчика = 4 
"""