'''
You are given a list of preferences for n friends, where n is always even.

For each person i, preferences[i] contains a list of friends sorted in the order of preference. In other words, a friend earlier in the list is more preferred than a friend later in the list. Friends in each list are denoted by integers from 0 to n-1.

All the friends are divided into pairs. The pairings are given in a list pairs, where pairs[i] = [xi, yi] denotes xi is paired with yi and yi is paired with xi.

However, this pairing may cause some of the friends to be unhappy. A friend x is unhappy if x is paired with y and there exists a friend u who is paired with v but:

x prefers u over y, and
u prefers x over v.
Return the number of unhappy friends.
'''

class Solution:
    # O(f^2) Time / O(f^2) Space
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        if n < 4:
            return 0
        prefTable = self.createTableOfPreferences(n, preferences, pairs)
        return self.getNumberOfUnhappyFriends(prefTable)
    
    # O(f^2) Time / O(f^2) Space
    def createTableOfPreferences(self, n, preferences, pairs):
        table = {}
        for friend in range(n):
            table[friend] = {"isHappy": True}
        for friend, preference in enumerate(preferences):
            for idx in range(len(preference)):
                table[friend][preference[idx]] = idx
        for pair in pairs:
            table[pair[0]]["partner"] = pair[1]
            table[pair[1]]["partner"] = pair[0]
        return table


    # O(f^2) Time / O(1) Space
    def getNumberOfUnhappyFriends(self, prefTable):
        count_of_unhappy_friends = 0
        for current_friend in list(prefTable.keys()):
            for possible_fellow in list(prefTable.keys()):
                current_fellow = prefTable[current_friend]["partner"]
                if possible_fellow == current_friend or possible_fellow == current_fellow:
                    continue
                if prefTable[current_friend][current_fellow] < prefTable[current_friend][possible_fellow]:
                    continue
                partner_of_possible_fellow = prefTable[possible_fellow]["partner"]
                if prefTable[possible_fellow][current_friend] > prefTable[possible_fellow][partner_of_possible_fellow]:
                    continue
                if prefTable[current_friend]["isHappy"]:
                    count_of_unhappy_friends += 1
                    prefTable[current_friend]["isHappy"] = False
                    break
        return count_of_unhappy_friends
    
