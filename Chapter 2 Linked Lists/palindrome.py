from linked_list import *

if __name__ == '__main__':
    llist = LinkedList()
    llist.add(7)
    llist.add(1)
    llist.add(7)
    rllist = llist
    temp1 = llist.head
    rllist.reverse()
    temp2 = rllist.head
    while(temp1 is not None):
        if(temp1.data != temp2.data):
            print("Not a palindrome!")
            break
        temp1 = temp1.next
        temp2 = temp2.next

    if(temp1 is None):
        print("It is a palindrome!")
