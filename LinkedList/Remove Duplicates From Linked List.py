'''
From
None->1->1->1->2->3->4->4->4->5->6->None
To
None->1->2->3->4->5->6->None
'''


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
	if linkedList is None or linkedList.next is None:
		return linkedList
    current_node = linkedList
	next_node = linkedList.next
	while next_node is not None:
		if current_node.value == next_node.value:
			next_node = next_node.next
			current_node.next = next_node
		else:
			current_node = current_node.next
			next_node = next_node.next

	return linkedList
		
		
		
		
		
