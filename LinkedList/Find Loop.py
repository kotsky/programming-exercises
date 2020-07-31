'''
You have a head of a linked list. You might assume that it contains LL loop.
Find its head.
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# Version 1.
# Counting +1 and +2 steps through linked list until pointer1 => pointer2.
# Then, move +1 from the head + pointer2 until they meet.

def findLoop(head):
  first = head.next
	second = head.next.next
	while first != second:
		first = first.next
		second = second.next.next
	first = head
	while first != second:
		first = first.next
		second = second.next
	return first
	
  
  '''
  # Version 2. With memorisation via hashtable.
  # This is an input class. Do not edit.

def findLoop(head):
  path = {}
	node = head
	while node not in path:
		path[node] = node.value
		if node.next is None:
			break
		node = node.next 
	return node

  '''
