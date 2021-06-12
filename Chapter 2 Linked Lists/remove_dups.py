from linked_list import *

if __name__ == '__main__':
    llist = createLinkedList([1, 2, 3, 4, 1])
    llist = removeNode(llist, 1)
    printLinkedList(llist)
