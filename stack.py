



class Stack (object):
    def __init__ (self):
        self.stack = []

# add an item to the top of the stack
    def push (self, item):
        self.stack.append (item)

  # remove an item from the top of the stack
    def pop (self):
        return self.stack.pop()

  # check the item on the top of the stack
    def peek (self):
        return self.stack[-1]

  # check if the stack is empty
    def is_empty (self):
        return (len(self.stack) == 0)

  # return the number of elements in the stack
    def size (self):
        return (len (self.stack))

from collections import deque
 
stack = deque()
 
# append() function to push
# element in the stack
stack.append('a')
stack.append('b')
stack.append('c')
 
print('Initial stack:')
print(stack)
 
# pop() fucntion to pop
# element from stack in 
# LIFO order
print('\nElements poped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())
 
print('\nStack after elements are poped:')
print(stack)
 
# uncommenting print(stack.pop())  
# will cause an IndexError 
# as the stack is now empty




