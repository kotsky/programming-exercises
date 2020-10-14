# Failed: 55 mins / why: missed inner counting and small errors. 
# General concept and coding structure were correct.

'''
Split LinkedList on half and reverse it in build.
Input: 0 -> 1 -> 2 -> 3 -> 4 -> 5 
Output: 2 -> 1 -> 0 -> 5 -> 4 -> 3

or

Input: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> 6
Output: 2 -> 1 -> 0 -> 3 -> 6 -> 5 -> 4

Idea:
1) Count total number of nodes
2) Split LL on 2 parts + mid node if there is
3) Reverse each part of LL
4) Attach them accordingly

'''


def invertedBisection(head):
    # step 1
    total_nodes, tail = specialLLTraverseToCountNodes(head)
    if total_nodes <= 2:
        return head

    if total_nodes % 2 == 0:
        middle_node = False
    else:
        middle_node = True
    count = total_nodes // 2
    new_head, new_tail, mid = specialLLTraverseToFindNewHeadTail(head, count, middle_node)

    # step 2
    new_head, partOneTail = reassignLLNodesInReverse(head, new_head, total_nodes)
    partTwoHead, new_tail = reassignLLNodesInReverse(new_tail, tail, total_nodes)
    # new_tail.next = None

    connectPartsOfLL(partOneTail, mid, partTwoHead)
    return new_head


def reassignLLNodesInReverse(head, tail, count):
    p0 = head
    p1 = p0.next
    p0.next = None
    inner_count = 1
    while p1 is not None and inner_count < count // 2:
        p2 = p1.next
        p1.next = p0
        p0 = p1
        p1 = p2
        inner_count += 1
    return tail, head


def connectPartsOfLL(partOneTail, mid, partTwoHead):
    if mid is None:
        partOneTail.next = partTwoHead
    else:
        partOneTail.next = mid
        mid.next = partTwoHead


def specialLLTraverseToFindNewHeadTail(head, count, isMid):
    inner_count = 1
    node = head
    new_head = None
    new_tail = None
    mid = None

    while node is not None:
        if inner_count == count:
            new_head = node
        elif inner_count == (count + 1):
            if isMid:
                mid = node
            else:
                new_tail = node
        elif inner_count == (count + 2):
            if isMid:
                new_tail = node
        node = node.next
        inner_count += 1

    return new_head, new_tail, mid


def specialLLTraverseToCountNodes(head):
    if head is None:
        return 0, None
    node = head
    count = 0
    while node is not None:
        prev = node
        node = node.next
        count += 1
    tail = prev
    return count, tail



class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None
