"""
You are given some middle node from a singly linked list.
Delete this node (3):
None->1->2->3->4->5->6->None
None->1->2->4->5->6->None

The idea 1: swap node's values to the end and then remove
the last node by pointing prev node to None.

The idea 2: swap node value with next node. And
point this node to the node after node.next.

Example:
    node = LinkedListNode(1)
    node.next = LinkedListNode(2)
    node.next.next = LinkedListNode(3)
    node_mid = node.next.next
    node_mid.next = LinkedListNode(4)
    node_mid.next.next = LinkedListNode(5)
    node_mid.next.next.next = LinkedListNode(6)
    
    
    printLinkedList(node)
    # printLinkedList(node_mid)
    
    deleteNodeFromSinglyLinkedListV2(node_mid)
    printLinkedList(node)
    # printLinkedList(node_mid)
"""


def printLinkedList(head):
    node = head
    print("None", end="->")
    while node is not None:
        print(node.value, end="->")
        node = node.next
    print("None")


class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(k) Time / O(1) Space

def deleteNodeFromSinglyLinkedListV1(node):
    def swapValues(nodeOne, nodeTwo):
        temp = nodeOne.value
        nodeOne.value = nodeTwo.value
        nodeTwo.value = temp

    prev_node = None
    while node.next is not None:
        prev_node = node
        swapValues(node, node.next)
        node = node.next
    prev_node.next = None
    node = None


# O(1) Time / Space

def deleteNodeFromSinglyLinkedListV2(node):
    prev_node = node
    temp = node.value
    node.value = node.next.value
    node.next.value = temp
    prev_node.next = node.next.next
