from linked_list import *

if __name__ == '__main__':
    temp1 = llist = createLinkedList([7, 1, 6, 1, 7])
    temp2 = rllist = reverseLinkedList(createLinkedList([7, 1, 6, 1, 7]))
    while(temp1 is not None):
        if(temp1.data != temp2.data):
            print("Not a palindrome!")
            break
        temp1 = temp1.next
        temp2 = temp2.next

    if(temp1 is None):
        print("It is a palindrome!")
