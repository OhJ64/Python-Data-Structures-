

#L33t code python solution to reverse a linked list
#using iteration 

def reverse(self, head):
    prev = None
    while head:
        temp = head
        head = head.next
        temp.next = prev
        prev = temp
    return prev


