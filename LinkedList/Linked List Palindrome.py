"""
You are given a Singly Linked List. Find out, if this SLL is palindrome.

The idea:
    1. Count length of SLL.
    2. Split SLL on 2 parts.
    3. Reverse 2nd part of SLL.
    4. Compare node by node in a sequence => it will give your answer.
    5* return the initial Singly Linked List in its order
        1) Reverse back 2nd part of SLL.
        2) Merge them (don't need, bcos I didn't point tail of 1st part
        onto None value - it still points to the tail of reversed 2nd SLL).

Example:
    node = LinkedListNode(3)
    node.next = LinkedListNode(1)
    node.next.next = LinkedListNode(2)
    node_mid = node.next.next
    node_mid.next = LinkedListNode(3)
    # node_mid.next.next = LinkedListNode(2)
    # node_mid.next.next.next = LinkedListNode(1)

    printLinkedList(node)

    output = linkedListPalindromeCheck(node)
    print(output)
    printLinkedList(node)
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


# O(N) Time / O(1) Space

def linkedListPalindromeCheck(head):
    def countLength(head):
        node = head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    def getMiddleNode(head):
        length = countLength(head)
        middle = length // 2
        node = head
        while middle > 0:
            node = node.next
            middle -= 1
        return node

    def reverseSinglyLinkedList(head):
        p1 = None
        p2 = head
        p3 = head.next
        while p2 is not None:
            p2.next = p1
            p1 = p2
            p2 = p3
            if p3 is None:
                break
            p3 = p3.next
        return p1

    def areTwoPartsSinglyLinkedListSame(head_one, head_two):
        p1 = head_one
        p2 = head_two

        while p1 is not None and p2 is not None:
            if p1.value == p2.value:
                p1 = p1.next
                p2 = p2.next
                continue
            else:
                return False
        return True

    new_head = getMiddleNode(head)
    new_head = reverseSinglyLinkedList(new_head)
    is_palindrome = areTwoPartsSinglyLinkedListSame(head, new_head)
    # reverse back to initial linked list
    new_head = reverseSinglyLinkedList(new_head)
    return is_palindrome
