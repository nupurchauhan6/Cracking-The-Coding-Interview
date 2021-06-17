from linked_list import *

if __name__ == '__main__':
    llist = LinkedList()
    llist.add(3)
    llist.add(5)
    llist.add(8)
    llist.add(10)
    llist.add(2)
    llist.add(1)
    partition = 5
    temp = llist.head
    less = LinkedList()
    more = LinkedList()
    rear = None
    while(temp is not None):
        data = temp.get_data()
        if(data < partition):
            less.add(data)
            if(less.head is not None and rear is None):
                rear = less.head
            rear = rear.get_next()
        else:
            more.add(data)
        temp = temp.get_next()
    if(rear is not None):
        rear.set_next(more.head)
        less.display()
    else:
        more.display()
