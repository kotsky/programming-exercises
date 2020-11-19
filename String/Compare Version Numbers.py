'''
Compare two version numbers version1 and version2.

If version1 > version2 return 1,
If version1 < version2 return -1,
otherwise return 0.
You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Here is an example of version numbers ordering:

0.1 < 1.1 < 1.2 < 1.13 < 1.13.4

string1 = "13.0"
string2 = "13.0..8"
print(compareVersion(string1, string2))

'''


def compareVersion(string_one, string_two):
    def convertVersionToNumber(string):
        version = string.split('.')
        for idx in range(len(version)):
            if version[idx]:
                try:
                    version[idx] = int(version[idx])
                except:
                    version[idx] = ord(version[idx])
            else:
                version[idx] = 0
        return version

    p1 = 0
    p2 = 0

    version_one = convertVersionToNumber(string_one)
    version_two = convertVersionToNumber(string_two)

    while p1 < len(version_one) and p2 < len(version_two):
        if version_one[p1] == version_two[p2]:
            p1 += 1
            p2 += 1
        elif version_one[p1] < version_two[p2]:
            return -1
        else:
            return 1

    if p1 == len(version_one) and p2 == len(version_two):
        return 0
    elif p1 == len(version_one):
        while p2 < len(version_two):
            if version_two[p2] != 0:
                return -1
            p2 += 1
        return 0
    else:
        while p1 < len(version_one):
            if version_one[p1] != 0:
                return 1
            p1 += 1
        return 0
    
