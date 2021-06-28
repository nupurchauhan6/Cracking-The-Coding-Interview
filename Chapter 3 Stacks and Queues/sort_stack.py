from stack import *

if __name__ == '__main__':
    stack = Stack()
    stack.push(5)
    stack.push(6)
    stack.push(1)
    min = stack.peek()
    temp = Stack()
    while(not temp.is_empty()):
        if(stack.peek() < min):
            temp.push(stack.pop())
    stack.display()
