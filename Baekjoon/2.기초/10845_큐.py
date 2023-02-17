MAX_QSIZE = 10
class CircularQueue :
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE
        
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear+1)%MAX_QSIZE
    
    def clear(self):
        self.front = self.rear
        
    def __len__(self):
        return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % MAX_QSIZE
            self.items[self.rear] = item
            
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]
        
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]