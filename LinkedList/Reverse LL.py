# 3 pointer and do a proper linking

def reverseLinkedList(head):
  parent_node = None
	node = head
	while node is not None:
		next_node = node.next
		node.next = parent_node
		parent_node = node
		node = next_node
	return parent_node
