class Vector(list):
    def __init__(self, items):
        super().__init__(items)
        self.dim = self.__len__() 

    def dot(self, other):
        if self.dim != other.dim:
            raise RuntimeError("두 벡터의 길이가 달라요!")
        sum = 0
        for i in range(self.dim):
            sum += self[i] * other[i]
        return sum
    
    def append(self, new_item):
        super().append(new_item)
        self.dim = self.__len__()

    def pop(self, idx=-1):
        removed_item = super().pop(idx)
        self.dim = self.__len__()
        return removed_item

    def __add__(self, other):
        if self.dim != other.dim:
            raise RuntimeError("두 벡터의 길이가 달라요!")
        new_list = []
        for i in range(self.dim):
            item = self[i] + other[i]
            new_list.append(item)
        return Vector(new_list)

    def __mul__(self, other):
        if self.dim != other.dim:
            raise RuntimeError("두 벡터의 길이가 달라요!")
        new_list = []
        for i in range(self.dim):
            item = self[i] * other[i]
            new_list.append(item)
        return Vector(new_list)
    
    def mean(self):
        return sum(self) / self.dim
    
x = Vector([2, 3, 4])
y = Vector([5, 6, 9])

print(x + y)
print(x * y)
print(Vector.mean(y))