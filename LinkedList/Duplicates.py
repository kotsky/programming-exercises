'''
Remove duplicates in Singly Linked List.

ll = SinglyLinkedList()
ll.generateRandomSinglyLinkedList(10)
ll.printLinkedList()
ll.removeDuplicatesWithNoMemoryUsage()
ll.printLinkedList()
'''

class SinglyLinkedList:
    class LinkedListNode:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None
        self.is_sorted = False

    def generateRandomSinglyLinkedList(self, size):
        import random
        for i in range(size):
            val = random.random()
            val = int(val * 10)
            self.addNode(val)
        self.is_sorted = False

    def addNode(self, value):
        node = self.LinkedListNode(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.is_sorted = False

    def removeInLine(self, prev_node, node):
        prev_node.next = node.next
        node = None
        return prev_node.next

    # Sort and use property of sorted array.
    # Time O(sort + N) / Space (sort + 1)
    # Possible to use merge sort or bubble sort.
    def removeDuplicatesWithNoMemoryUsage(self):
        if self.head is None:
            print("There is not Linked List to sort. Please, add nodes")
            return
        if self.is_sorted is False:
            self.sortBubble()
        node = self.head.next
        prev_node = self.head
        while node is not None:
            if prev_node.value == node.value:
                node = self.removeInLine(prev_node, node)
            else:
                node = node.next
                prev_node = prev_node.next

    # Use hast table to track same values.
    # Time O(N) worst / Space O(n), where n - number of unique values
    def removeDuplicates(self, clean_memo=False):
        if self.head is None:
            return
        table_of_nodes = {}
        node = self.head.next
        prev_node = self.head
        table_of_nodes[prev_node.value] = True
        while node is not None:
            if node.value in table_of_nodes:
                node = self.removeInLine(prev_node, node)
            else:
                table_of_nodes[node.value] = True
                node = node.next
                prev_node = prev_node.next

        if clean_memo:
            for key in table_of_nodes:
                del table_of_nodes[key]

    def swapInPlace(self, node_one, node_two):
        temp = node_two.value
        node_two.value = node_one.value
        node_one.value = temp
        temp = None
        self.is_sorted = False

    # Bubble algorithms: Time O(N^2) worst / Space O(1)
    def sortBubble(self):
        if self.head is None:
            print("There is not Linked List to sort. Please, add nodes")
            return
        if self.is_sorted:
            # print("This Singly Linked List is sorted")
            return
        is_sorted = False
        while is_sorted is False:
            is_sorted = True
            node = self.head
            while node.next is not None:
                if node.value > node.next.value:
                    self.swapInPlace(node, node.next)
                    is_sorted = False
                node = node.next
        self.is_sorted = True

    def sortMerge(self):
        if self.is_sorted:
            print("There is not Linked List to sort. Please, add nodes")
            return
        self.is_sorted = True
        return self.sortMergeHelper(self.head)

    def sortMergeHelper(self, head_one):
        if head_one is None or head_one.next is None:
            return head_one

        middle_node = self.getMiddle(head_one)
        head_two = middle_node.next
        middle_node.next = None
        head_one = self.sortMergeHelper(head_one)
        head_two = self.sortMergeHelper(head_two)
        self.head = self.mergeSortedSinglyLinkedLists(head_one, head_two)
        return self.head

    def mergeSortedSinglyLinkedLists(self, head_one, head_two):
        if head_one is None or head_two is None:
            return head_two if head_two is not None else head_one

        p1 = head_one
        p1_prev = None
        p2 = head_two
        while p1 is not None and p2 is not None:
            if p1.value < p2.value:
                p1_prev = p1
                p1 = p1.next
            else:
                if p1_prev is not None:
                    p1_prev.next = p2
                p1_prev = p2
                p2 = p2.next
                p1_prev.next = p1
        if p1 is None:
            p1_prev.next = p2
        return head_one if head_one.value < head_two.value else head_two

    # Utility function to get the middle
    # of the linked list
    def getMiddle(self, head):
        if head is None:
            return head

        slow = head
        fast = head

        while fast.next is not None and \
                fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def printLinkedList(self):
        node = self.head
        print("None", end="->")
        while node is not None:
            print(node.value, end="->")
            node = node.next
        print("None")
