class OneDArray:
    def __init__(self, items):
        self.items = list(items)
        self.count = 0
        self.max_repeats = len(items)

    def __repr__(self):
        return f"myArray({self.items})"

    def __add__(self, other):
        if len(self.items) != len(other.items):
            raise RuntimeError("길이가 달라요!")
        main_object = self.items.copy()
        for i in range(len(main_object)):
            main_object[i] += other.items[i]
        return OneDArray(main_object)

    def __len__(self):
        return len(self.items)

    def mean(self):
        sum = 0
        for item in self.items:
            sum += item
        return sum/len(self)

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.max_repeats:
            self.count = 0					  #반복문 실행을 위해 추가한 항목
            raise StopIteration("더 이상 항목이 없어요!")
        next_item = self.items[self.count]
        self.count += 1  
        return next_item

oneD1 = OneDArray([2, 3, 4])
oneD2 = OneDArray([11, 22, 33])
oneD3 = oneD1 + oneD2
for x in oneD3:
    print(x)
    
for x in oneD3:
    print(x)