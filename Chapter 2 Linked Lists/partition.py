from linked_list import *

if __name__ == '__main__':
    llist = createLinkedList([3, 5, 8, 5, 10, 2, 1])
    partition = 5
    temp = llist
    less = more = pless = pmore = None
    while(temp is not None):
        tNode = Node(temp.data)
        if(temp.data < partition):
            if(less is None):
                less = pless = tNode
            else:
                pless.next = tNode
                pless = pless.next

        else:
            if(more is None):
                more = pmore = tNode
            else:
                pmore.next = tNode
                pmore = pmore.next
        temp = temp.next

    pless.next = more
    printLinkedList(less)
