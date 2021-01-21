
class Link (object):
  def __init__ (self, data, next = None):
    self.data = data
    self.next = next

class LinkedList (object):
  def __init__ (self):
    self.first = None

  # add data at the beginning
  def insert_first (self, data):
    new_link = Link (data)

    new_link.next = self.first
    self.first = new_link

  # add data at the end
  def insert_last (self, data):
    new_link = Link (data)

    current = self.first
    if (current == None):
      self.first = new_link
      return

    while (current.next != None):
      current = current.next

    current.next = new_link

  # find data in a linked list
  def find_link (self, data):
    current = self.first

    if (current == None):
      return None

    while (current.data != data):
      if (current.next == None):
        return None
      else:
        current = current.next

    return current

  # delete link with given data
  def delete_link (self, data):
    previous = self.first
    current = self.first

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

