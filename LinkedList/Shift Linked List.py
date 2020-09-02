'''
Shift LL by factor k.
1->2->3->4 by 2 => 3->4->1->2
'''

def shiftLinkedList(head, k):
    if head.next is None or head is None:
        return head
    ll_lenght = 0
    node = head
    while node is not None:
        ll_lenght += 1
        if node.next is None:
            tail = node
        node = node.next

    k = k % ll_lenght
    if k == 0:
        return head

    shiftBy = ll_lenght - k if k > 0 else -k
    tail.next = head
    counter = 0
    node = head
    while counter < shiftBy - 1:
        node = node.next
        counter += 1
    head = node.next
    node.next = None
    return head


# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
