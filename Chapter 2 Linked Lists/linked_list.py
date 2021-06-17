class Node:

    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = newdata

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        if(self.is_empty()):
            self.head = temp
        else:
            current = self.head
            while(current.get_next() is not None):
                current = current.get_next()
            current.set_next(temp)

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current is not None:
            if(current.get_data() == item):
                found = True
            else:
                previous = current
                current = current.get_next()
        if(not found):
            return
        if(previous == None):
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def display(self):
        current = self.head
        while(current is not None):
            print(current.get_data())
            current = current.get_next()

    def reverse(self):
        first = current = self.head
        previous = ahead = None
        while(current is not None):
            ahead = current
            current = current.next
            if previous is not None:
                ahead.set_next(previous)
            if(previous == first):
                previous.set_next(None)
                self.head.set_next(None)
            self.head = previous = ahead
