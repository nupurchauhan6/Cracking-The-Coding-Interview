from linked_list import *

if __name__ == '__main__':
    inputNode = Node("c")
    llist = createLinkedList(["a", "b", "c", "d", "e"])
    llist = removeNode(llist, inputNode.data)
    printLinkedList(llist)
