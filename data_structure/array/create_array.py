class MyArray:
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return str(self.__dict__)

    def push(self,item):
        self.data[self.length] = item
        self.length += 1

    def get(self,index):
        return self.data[index]

    def pop(self):
        lastItem = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return lastItem

    def deleteItem(self,index):
        delItem = self.data[index]
        for i in range(index, self.length - 1):
            self.data[i] = self.data[i+1]

        del self.data[self.length - 1]
        self.length -= 1
        return delItem

arr = MyArray()
arr.push(1)
arr.push(2)
arr.push(3)
arr.push(4)
print(arr)
print(arr.get(2))
arr.pop()
print(arr)
print(arr.deleteItem(1))
print(arr)