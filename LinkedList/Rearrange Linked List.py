'''
Rearrange LL in a way that all node with values less than k are from the left side of the LL, and others are from the right side as the following:
3->0->5->2->1->4 => [0, 2, 1, 3, 5, 4]  if k = 3
or
3->0->5->2->1->4 => [3, 0, 2, 1, 4, 5]  if k = 4 || imagine 3.5.
Nodes have to be in the same order in respect to their affiliation.

The idea is to split LL onto 3 parts, build each separated LL (node.value < k), (node.value = k) and (node.value > k).
Then, combine 3 parts into one finale LL.
Be aware, that there might be duplicates or no existing of k value node.
'''

def rearrangeLinkedList(head, k):
    # Step 1: create heads/tails
    small_head = None
    small_tail = None
    mid_head = None
    mid_tail = None
    large_head = None
    large_tail = None

    # Step 2: traverse ll and repoint elements accordingly
    node = head
    while node is not None:
        if node.value < k:
            small_head, small_tail = adjustLocalLinkedList(small_head, small_tail, node)
        elif node.value == k:
            mid_head, mid_tail = adjustLocalLinkedList(mid_head, mid_tail, node)
        else:
            large_head, large_tail = adjustLocalLinkedList(large_head, large_tail, node)
        node = node.next

    # Step 3: build the finale linked list from 3 parts
    first_head, first_tail = connectLinkedLists(small_head, small_tail, mid_head, mid_tail)
    finale_head, _ = connectLinkedLists(first_head, first_tail, large_head, large_tail)
    _.next = None
    return finale_head


def connectLinkedLists(head1, tail1, head2, tail2):
    head = head2 if head1 is None else head1
    tail = tail1 if tail2 is None else tail2

    if tail1 is not None:
        tail1.next = head2

    return head, tail


def adjustLocalLinkedList(head, tail, node):
    if head is None:
        head = node
        tail = head
    else:
        tail.next = node
        tail = tail.next
    return head, tail


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListToArray(head):
    array = []
    current = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array


head = LinkedList(3)
head.next = LinkedList(0)
head.next.next = LinkedList(5)
head.next.next.next = LinkedList(2)
head.next.next.next.next = LinkedList(1)
head.next.next.next.next.next = LinkedList(4)
result = rearrangeLinkedList(head, 3)
array = linkedListToArray(result)


print(array)
