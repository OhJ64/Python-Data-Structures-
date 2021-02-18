

class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next


class LinkedList (object):
  def __init__ (self):
    self.first = None

  def insertFirst (self, data):
    newLink = Link (data)
    newLink.next = self.first
    self.first = newLink

  def insertLast (self, data):
    newLink = Link (data)
    current = self.first

    if (current == None):
      self.first = newLink
      return

    while (current.next != None):
      current = current.next

    current.next = newLink

  def findLink (self, data):
    current = self.first
    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  def deleteLink (self, data):
    current = self.first
    previous = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        previous = current
	current = current.next

    if (current == self.first):
      self.first = self.first.next
    else:
      previous.next = current.next

    return current


#* Application of Linked Lists
#  - implementation of Stacks and Queues in constant time
 # - Denote connectivity of vertices in a graph - adjacency list
 # - Sparse matrix representation 
  #- Compact Hash Table
  #- Dynamic memory allocation - linked list of free blocks

#* Doubly Linked List
 # - Link has now next and previous pointers
  #- traverse both ways in the linked list

