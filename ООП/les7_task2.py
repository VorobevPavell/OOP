class Stack():
    
    def __init__(self) -> None:
        self.values = []

    def push(self,item):
        self.values.append(item)

    def pop(self):
        if len(self.values) == 0:
            print('Empty Stack')
        return self.values.pop(-1)

    def peek(self):
        if len(self.values) != 0:
            return self.values[-1]
        print('Empty Stack')
        return None


    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)

s = Stack()
s.peek()
print(s.is_empty())
s.push('cat')
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(777)
print(s.pop())
print(s.pop())
print(s.size())