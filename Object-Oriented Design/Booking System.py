'''

Booking system for one hotel room

'''


class BookingSystem:

    class BST:

        class Node:
            def __init__(self, check_in, check_out):
                self.check_in = check_in
                self.check_out = check_out
                self.left = None
                self.right = None

        def __init__(self):
            self.root = None

        def search(self):
            pass

        def insert(self, new_node):
            if self.root is None:
                self.root = new_node
                return True

            current_node = self.root
            parent_node = None

            while current_node is not None:
                if current_node.check_in < new_node.check_in:

                    if new_node.check_in <= current_node.check_out:
                        return False

                    parent_node = current_node
                    current_node = current_node.right

                elif current_node.check_in > new_node.check_in:

                    if current_node.check_in <= new_node.check_out:
                        return False

                    parent_node = current_node
                    current_node = current_node.left
                else:
                    return False

            if parent_node.check_in > new_node.check_in:
                parent_node.left = new_node
            else:
                parent_node.right = new_node

            return True

    def __init__(self):
        self.schedule = BookingSystem.BST()  # some DB

    def add(self, check_in: int, check_out: int) -> bool:
        '''
        Do room booking according to given date in and out
        :param check_in: start time
        :param check_out: end time
        :return: True if booking succeed, False - if the room in unavailable
        '''

        possible_booking_interval = BookingSystem.BST.Node(check_in, check_out)
        return self.schedule.insert(possible_booking_interval)


bs = BookingSystem()
bs.add(3, 10)
print(bs.add(0, 2))
print(bs.add(6, 12))
