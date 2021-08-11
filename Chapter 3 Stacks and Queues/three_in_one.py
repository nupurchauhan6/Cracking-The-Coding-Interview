from stack import *


def fillStack(array, stack):
    for ele in array:
        stack.push(ele)


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 8]
    n = len(array)
    array1 = array[0:int(n/3)]
    array2 = array[int(n/3):int(2*n/3)]
    array3 = array[int(2*n/3):n]
    stack1 = Stack()
    stack2 = Stack()
    stack3 = Stack()
    fillStack(array1, stack1)
    fillStack(array2, stack2)
    fillStack(array3, stack3)
    print("First")
    stack1.display()
    print("Second")
    stack2.display()
    print("Third")
    stack3.display()
