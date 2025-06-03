class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit
        pass

    def isEmpty(self):
        if self.size() == 0:
            return True
        return False

    def push(self, item):
        if not self.full():
            self.items.append(item)
        return

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None
    
    def size(self):
        return len(self.items)

    def full(self):
        if self.size() == self.limit:
            return True 
        return False 

    def search(self, target):
        if self.isEmpty():
            return -1
        if self.peek() == target:
            return 0
        for i in range(1,len(self.items)):
            if self.items[i-1] == target:
                return len(self.items) - i
        return -1
        
            
