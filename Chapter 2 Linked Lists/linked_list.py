class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def createLinkedList(llist):
    head = prev = None
    for ele in llist:
        temp = Node(ele)
        if(head == None):
            head = prev = temp
        else:
            prev.next = temp
        prev = temp
    return head


def printLinkedList(llist):
    temp = llist
    while(temp is not None):
        print(temp.data)
        temp = temp.next


def getLinkedListSize(llist):
    temp = llist
    i = 0
    while(temp is not None):
        i = i + 1
        temp = temp.next
    return i


def removeNode(llist, data):
    head = temp = prev = llist
    if(head.data == data):
        head = temp.next
        temp = temp.next
    while(temp is not None):
        if(temp.data == data):
            prev.next = temp.next
        prev = temp
        temp = temp.next
    return head
