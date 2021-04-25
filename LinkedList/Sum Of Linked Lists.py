'''
Build new Single Linked List by adding 2 others:
1->7->4 (like 471 number)
9->9->1 (like 199 number)
0->7->6 (670)

'''

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
  new_ll = LinkedList(0)
	remain = 0
	new_ll_node = new_ll
	ll1_node = linkedListOne
	ll2_node = linkedListTwo
	while True:
		ll1_value = ll1_node.value if ll1_node is not None else 0
		ll2_value = ll2_node.value if ll2_node is not None else 0
		
		new_value = ll1_value + ll2_value + remain
		
		remain = new_value // 10
		new_value %= 10
		
		new_ll_node.value = new_value
		
		ll1_node = ll1_node.next if ll1_node is not None else None
		ll2_node = ll2_node.next if ll2_node is not None else None
		
		if ll1_node is not None or ll2_node is not None or remain != 0:
			new_ll_node.next = LinkedList(0)
			new_ll_node = new_ll_node.next
		else:
			break
	
    return new_ll

