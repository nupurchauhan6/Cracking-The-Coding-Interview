from linked_list import *


def reverse_order(llist1, llist2):
    llist1.reverse()
    llist2.reverse()
    forward_order(llist1, llist2)


def forward_order(llist1, llist2):
    temp1 = llist1.head
    temp2 = llist2.head
    str1 = str2 = ""
    sum = 0
    while(temp1 is not None):
        str1 = str1 + str(temp1.get_data())
        str2 = str2 + str(temp2.get_data())
        temp1 = temp1.get_next()
        temp2 = temp2.get_next()
    sum = int(str1) + int(str2)
    ans = [int(x) for x in str(sum)]
    fllist = LinkedList()
    for ele in ans:
        fllist.add(ele)
    fllist.display()


if __name__ == '__main__':
    llist1 = LinkedList()
    llist2 = LinkedList()
    llist1.add(7)
    llist1.add(1)
    llist1.add(6)
    llist2.add(5)
    llist2.add(9)
    llist2.add(2)
    reverse_order(llist1, llist2)
    forward_order(llist1, llist2)
