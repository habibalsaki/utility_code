class Node:
    """[summary]

    """
    def __init__(self,data):
        self.value = data
        self.next = None

    def __str__(self):
        return str(self.__dict__)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def append(self, item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1

    def prepend(self,item):
        new_node = Node(item)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length += 1
        else:
            new_node.next = self.head
            self.head = new_node
            self.length += 1

    def insert(self,item,index):
        if index >= self.length:
            self.append(item)
        elif index == 0:
            self.prepend(item)
        else:
            i = 0
            temp = self.head
            new_node = Node(item)
            while i < self.length:
                if i == index - 1:
                    temp.next, new_node.next = new_node, temp.next
                    self.length += 1
                    break 
                i += 1
                temp = temp.next

    def remove(self, index):
        if index >= self.length:
            print("LinkedList is not this long")
            return None
        elif index == 0:
            self.head = self.head.next
            self.length -= 1
            return None

        else:
            i = 0
            temp = self.head

            while i <= self.length:
                if i == index - 1:
                    temp.next = temp.next.next
                    self.length -= 1
                    break
                i += 1
                temp = temp.next
            return None

    def printl(self):
        temp = self.head
        while temp is not None:
            print(temp.value,sep=" ")
            temp = temp.next
        print()
        print(f"Length is {self.length}")

llist = LinkedList()
llist.append(10)
llist.append(5)
llist.append(15)
llist.prepend(20)
llist.insert(16,2)
llist.remove(2)
llist.printl()