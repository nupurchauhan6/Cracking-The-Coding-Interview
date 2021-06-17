from linked_list import *

if __name__ == '__main__':
    llist = LinkedList()
    llist.add(1)
    llist.add(2)
    llist.add(5)
    llist.add(7)
    head = temp = llist.head
    k = 3
    i = 1
    ans = LinkedList()
    while(temp is not None):
        if(k == i):
            ans.head = temp
            break
        i = i + 1
        temp = temp.next
    if(temp is None):
        ans.head = None
    ans.display()
