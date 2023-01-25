from math import sqrt


class Point():

    list_points = []

    def __init__(self,coord_x=0,coord_y=0):
        self.move_to(coord_x,coord_y)
        Point.list_points.append(self)

    def move_to(self,new_x,new_y):
        self.x = new_x
        self.y = new_y

    def reset(self):
        self.move_to(0,0)

    def print_point(self):
        print(f"Точка с координатами {self.x} , {self.y}")
    def get_distance(self,another_point):
        if not isinstance(another_point,Point):
            raise ValueError('Передана не точка')
        return sqrt((self.x - another_point.x)**2 + (self.y - another_point.y)**2)

p1 = Point(12,4)
print(p1.x,p1.y)
p1.move_to(66,8)
print(p1.x,p1.y)
p1.print_point()
p1.reset()
p1.print_point()
p1.move_to(6,0)
p2 = Point(0,8)
print(p2.get_distance(p1))

print(Point.list_points[1].x,Point.list_points[1].y)
