from linked_list import *

if __name__ == '__main__':
    inputNode = Node("c")
    llist = LinkedList()
    llist.add("a")
    llist.add("b")
    llist.add("c")
    llist.add("d")
    llist.add("e")
    llist.remove(inputNode.get_data())
    llist.display()
