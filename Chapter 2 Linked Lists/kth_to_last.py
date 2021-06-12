from linked_list import *

if __name__ == '__main__':
    llist = createLinkedList([1, 3, 5, 6])
    head = temp = llist
    k = 2
    i = 1
    while(temp is not None):
        if(k == i):
            head = temp
            break
        i = i + 1
        temp = temp.next
    if(temp is None):
        head = None
    printLinkedList(head)
