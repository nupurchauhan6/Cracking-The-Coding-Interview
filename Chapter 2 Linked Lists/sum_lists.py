from linked_list import *


def reverse_order(llist1, llist2):
    llist1 = reverseLinkedList(llist1)
    llist2 = reverseLinkedList(llist2)
    forward_order(llist1, llist2)


def forward_order(llist1, llist2):
    temp1 = llist1
    temp2 = llist2
    str1 = str2 = ""
    sum = 0
    while(temp1 is not None):
        str1 = str1 + str(temp1.data)
        str2 = str2 + str(temp2.data)
        temp1 = temp1.next
        temp2 = temp2.next
    sum = int(str1) + int(str2)
    ans = [int(x) for x in str(sum)]
    printLinkedList(createLinkedList(ans))


if __name__ == '__main__':
    llist1 = createLinkedList([7, 1, 6])
    llist2 = createLinkedList([5, 9, 2])
    reverse_order(llist1, llist2)
    forward_order(llist1, llist2)
