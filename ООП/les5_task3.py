class Point():

    def set_coordinates(self,x,y): # принимает координаты по х и у и сохраняет в экземпляр класса в атрибуты х и у
        self.x = x
        self.y = y

    def get_distance(self,instance): # принимает экземпляр класса Point и возвращает расстояние между точками
        if isinstance(instance,Point):
            return ((self.x - instance.x) ** 2 + (self.y - instance.y) ** 2) ** 0.5
        else:
            return 'Передана не точка'


p1 = Point()
p2 = Point()
p1.set_coordinates(1,2)
p2.set_coordinates(4,6)
d = p1.get_distance(p2)
print(d)
print(p1.get_distance(10))

