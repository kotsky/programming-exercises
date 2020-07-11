from LinkedList import *


def bindNodes(nodeOne, nodeTwo):
    nodeOne.next = nodeTwo
    nodeTwo.prev = nodeOne


linkedList = DoublyLinkedList()
one = Node(1)
two = Node(2)
three = Node(3)
three2 = Node(3)
three3 = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
bindNodes(one, two)
bindNodes(two, three)
bindNodes(three, four)
bindNodes(four, five)
linkedList.head = one
linkedList.tail = five

def printLinkedList(node):
    print("None", end="<->")
    while node is not None:
        print(node.value, end="<->")
        node = node.next
    print("None")

printLinkedList(linkedList.head)    # None<->1<->2<->3<->4<->5<->None
