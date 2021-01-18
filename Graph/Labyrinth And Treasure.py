"""Labyrinth and treasure

Labyrinth with rooms, which are connected via doors.
Some doors are opened, some not. To open the door, you need
a key, which you can find in the labyrinth during its exploring.
Some doors can be opened by certain keys. Somewhere a treasure is hidden.

Can you find the treasure from start_room? -> True/False

The idea: starting from start_room, we do:
1. exploring the room:
2. collect all keys from that room;
3. to open each doors in that room:
    1) with all available keys, try open each room
    2) if fail to open the door -> keep door to be explored later
    3) if success to open the door -> delete this door from the queue
    of doors' exploring and add new room to explore
4. repeat until treasure is not found and we still have rooms to explore

To check solving of this problems, Labyrinth class was created to generate 
labyrinth with our initial inputs. For that particular labyrinth_data below, 
refer to https://github.com/kotsky/programming-exercises/blob/master/additional_data/graph_labyrinth_example_1.png

Example:
    labyrinth_data = [[0, [0], [6], None], [1, [1], [-1], None], [2, [2], [5], [0]],
                  [3, [3, 16], [-1, 2], [1]], [4, [7, 8], [1, -1], None],
                  [5, [7, 6, 9, 1], [1, -1, 7, -1], [3, 4]], [6, [2, 5, 16], [5, 3, 2], [2]],
                  [7, [3, 12], [-1, 3], [5, 6]], [8, [8], [-1], None],
                  [9, [9, 10], [7, 6], None], [10, [5, 6, 11], [3, -1, 2], None],
                  [11, [11, 12, 13], [2, 3, -1], None], [12, [13, 14], [-1, 0], [2]],
                  [13, [10, 14, 0, 4], [6, 0, 6, -1], [0]], [14, [4], [-1], [6]]]
	// according to the picture graph_labyrinth_example_1.png

    lab = Labyrinth(labyrinth_data)
    
    # set treasure in room_id = 4
    room_id = 4
    lab.labyrinth_rooms[room_id].is_treasure = True
    start_room_id = 1
    
    print(can_you_find_treasure(start_room_id, lab))

"""


class Room:

    def __init__(self, room_id):  # room_keys, room_doors):
        """
        :param room_id: room id as its identity
        """
        self.id = room_id
        self.keys = []   # keys, which are in the room
        self.doors = []   # doors in the room
        self.is_visited = False  # did we visit that room before?
        self.is_treasure = False  # is there a treasure

    def get_keys(self):
        return self.keys


class Door:

    def __init__(self, door_id):  # door_rooms, is_opened, keys_to_open_this_door):
        """
        :param door_id: door id as its identity

        Regarding keys_to_open_this_door:
            The logic - when we insert key, we can immediately
            find out, if this key is suitable for that door.
            That gives instant experience if you can open the door or no
        """
        self.id = door_id
        self.rooms = []  # rooms, which this door opens
        self.is_opened = False  # is the door opened?
        self.keys_to_open_this_door = {}  # set of key
        self.is_visited = False

    def to_open(self, list_of_keys):
        """
        Iterating over available keys
        :param list_of_keys:
        """
        for key in list_of_keys:
            if key in self.keys_to_open_this_door:
                self.is_opened = True

#
# class Key:
#
#     def __init__(self, key_id):
#         self.id = key_id


class Labyrinth:
    """
    This class helps to generate virtual labyrinth
    with fully connected rooms, doors and available
    keys there.

    :param labyrinth_data = [
                                [
                                    room_id,
                                    [doors_id from that room],
                                    [doors' properties: open (-1)? what key_id can open it?],
                                    [keys_id in the room]
                                ],
                                []
                            ]
    """

    def __init__(self, labyrinth_data):
        self.labyrinth_doors = {}
        self.labyrinth_keys = {}
        self.labyrinth_rooms = {}
        self.generate_keys(self.get_count_keys())
        self.generate_labyrinth(labyrinth_data)

    def generate_keys(self, size):
        for key in range(size+5):
            self.labyrinth_keys[key] = key

    def generate_labyrinth(self, labyrinth_data):
        for x in range(len(labyrinth_data)):
            room_idx, doors, type_of_doors, keys = labyrinth_data[x]
            current_room = Room(room_idx)

            # assign keys to room if there are keys
            if keys is not None:
                for key in keys:
                    current_room.keys.append(self.labyrinth_keys[key])

            # create doors as new entities and
            # assign doors to current room
            for idx in range(len(doors)):
                door_id = doors[idx]
                door_type_id = type_of_doors[idx]
                if door_id not in self.labyrinth_doors:
                    self.labyrinth_doors[door_id] = Door(door_id)
                door = self.labyrinth_doors[door_id]
                door.rooms.append(current_room)
                if door_type_id == -1:
                    door.is_opened = True
                else:
                    key = self.labyrinth_keys[door_type_id]
                    self.labyrinth_doors[door_id].keys_to_open_this_door[key] = key
                current_room.doors.append(door)

            self.labyrinth_rooms[room_idx] = current_room

    def get_count_keys(self):
        max_size = 0
        for x in range(len(labyrinth_data)):
            key_type = labyrinth_data[x][-1]
            if key_type is not None:
                for k in key_type:
                    max_size = max(max_size, k)
        return max_size


def can_you_find_treasure(start_room_id, labyrinth):

    def _get_collection(from_collection, to_collection, check_visiting=False):
        if type(to_collection) == type({}):
            for token in from_collection:
                to_collection[token.id] = token
        else:
            for token in from_collection:
                if check_visiting is True and token.is_visited is True:
                    continue
                to_collection.append(token)

    def _explore_doors():
        explored_doors = []
        for door_idx in list_of_doors_to_be_explored:
            door = list_of_doors_to_be_explored[door_idx]
            door.to_open(backpack)
            if door.is_opened is True:
                _get_collection(door.rooms, list_of_rooms_to_be_explored, True)
                explored_doors.append(door_idx)

        # no need to explore this door
        for door_idx in explored_doors:
            del list_of_doors_to_be_explored[door_idx]

    start_room = labyrinth.labyrinth_rooms[start_room_id]

    # backpack contains our found keys
    backpack = []

    list_of_doors_to_be_explored = {}
    list_of_rooms_to_be_explored = [start_room]
    current_room = None

    while list_of_rooms_to_be_explored:

        # explore current room
        current_room = list_of_rooms_to_be_explored.pop()
        current_room.is_visited = True
        # print(current_room.id)

        # return True if we found the treasure
        if current_room.is_treasure is True:
            return True

        # collect keys from the room
        _get_collection(current_room.get_keys(), backpack)
        # write down doors from the room
        _get_collection(current_room.doors, list_of_doors_to_be_explored)

        # try to open doors with available keys
        _explore_doors()
        # after that, you have new rooms to explore

    return False


labyrinth_data = [[0, [0], [6], None], [1, [1], [-1], None], [2, [2], [5], [0]],
                  [3, [3, 16], [-1, 2], [1]], [4, [7, 8], [1, -1], None],
                  [5, [7, 6, 9, 1], [1, -1, 7, -1], [3, 4]], [6, [2, 5, 16], [5, 3, 2], [2]],
                  [7, [3, 12], [-1, 3], [5, 6]], [8, [8], [-1], None],
                  [9, [9, 10], [7, 6], None], [10, [5, 6, 11], [3, -1, 2], None],
                  [11, [11, 12, 13], [2, 3, -1], None], [12, [13, 14], [-1, 0], [2]],
                  [13, [10, 14, 0, 4], [6, 0, 6, -1], [0]], [14, [4], [-1], [6]]]


lab = Labyrinth(labyrinth_data)

# set treasure in room_id = 4
room_id = 4
lab.labyrinth_rooms[room_id].is_treasure = True
start_room_id = 1

print(can_you_find_treasure(start_room_id, lab))
