'''
Merge 2 linkedlists witout additional memory.
'''


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    if headOne.value <= headTwo.value:
        mainHead = headOne
        nodeOne = headOne.next
        nodeTwo = headTwo
    elif headOne.value > headTwo.value:
        mainHead = headTwo
        nodeOne = headOne
        nodeTwo = headTwo.next

    parent = mainHead

    while nodeOne is not None and nodeTwo is not None:
        if nodeOne.value < nodeTwo.value:
            parent.next = nodeOne
            nodeOne = nodeOne.next
            parent = parent.next
        else:
            parent.next = nodeTwo
            nodeTwo = nodeTwo.next
            parent = parent.next

    if nodeOne is not None:
        parent.next = nodeOne
    elif nodeTwo is not None:
        parent.next = nodeTwo

    return mainHead
