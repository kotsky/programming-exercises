"""
Write a function, which will take 2 numbers in a singly linked list
format and return the gotten number in reverse in a format of linked list.
None->1->2->3->None     # 321
None->9->4->5->6->None  # 6549
None->7->8->6->None     # 321 + 6549 = 6870 => 7->8->6

The idea: convert two LL into numbers by adding each value with
multiplication by 10^(iteration). Sum up these numbers.
Then, reversed operation with new number to get LL, which
will be placed on place of the longest LL.
LL - linked list.

Example:
    node = LinkedListNode(1)
    node.next = LinkedListNode(2)
    node.next.next = LinkedListNode(3)
    node_mid = LinkedListNode(9)
    node_mid.next = LinkedListNode(4)
    node_mid.next.next = LinkedListNode(5)
    node_mid.next.next.next = LinkedListNode(6)

    printLinkedList(node)
    printLinkedList(node_mid)

    output = sumList(node, node_mid)
    printLinkedList(output)
"""

# O(N) Time, where N - number of elements in the longest
# linked list; O(1) Space (we replace values of the longest
# linked list with values from the finale linked list)

def sumList(head_one, head_two):
    
    # Find numbers from two linked lists 
    # 321 & 6549
    # and sum them to get finale number:
    # 321 + 6549 = 6870 => 7->8->6
    
    def findSumOfTwoLinkedLists(head_one, head_two):
        rang = 0
        node_one = head_one
        node_two = head_two
        ll_sum = 0
        one_is_longer = False
        while node_one is not None and node_two is not None:
            ll_sum += (node_one.value + node_two.value) * pow(10, rang)
            node_one = node_one.next
            node_two = node_two.next
            rang += 1

        while node_one is not None:
            ll_sum += node_one.value * pow(10, rang)
            node_one = node_one.next
            rang += 1
            one_is_longer = True

        while node_two is not None:
            ll_sum += node_two.value * pow(10, rang)
            node_two = node_two.next
            rang += 1
            one_is_longer = False

        print(ll_sum)
        return ll_sum, one_is_longer

    # Remove zero value from the head
    def adjustHead(head):
        while head.value == 0:
            head = head.next
        return head

    # Convert 6870 => 7->8->6 by replacing
    # value in the longest linked list (in place)
    
    def calculateReversedLinkedListAndInsertInPlace(head, suma):
        rang = 1
        node = head
        while suma > 9:
            rest = suma % pow(10, rang)
            node.value = rest
            suma = suma // pow(10, rang)
            node = node.next
        node.value = suma
        node.next = None

        head = adjustHead(head)

        return head

    ll_sum, one_is_longer = findSumOfTwoLinkedLists(head_one, head_two)
    if ll_sum == 0: # for None, None inputs
        return LinkedListNode(0)
    finale_linked_list = head_one if one_is_longer else head_two
    return calculateReversedLinkedListAndInsertInPlace(finale_linked_list, ll_sum)


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
