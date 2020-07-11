'''
To remove Nth node from the end of the given Singly Linked List
'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    
	totalElements = 0
	node = head
	
	while node is not None:
		node = node.next
		totalElements += 1
		
	passToK = totalElements - k
	counter = 0
	node = head
	
	if passToK >= 1:
		while counter != passToK-1:
			node = node.next
			counter += 1
	else:
		node.value = node.next.value
	
	node.next = node.next.next
	
	
