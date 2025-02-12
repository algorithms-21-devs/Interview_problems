""" Question
Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written
using the exact same letters (so you can just rearrange the letters to get a different phrase or word).
consider characters only to be lowercase only a-z
Test Cases:
"public relations" is an anagram of "crap built on lies."
"clint eastwood" is an anagram of "old west action"
"""

# Running time is O(n) + O(n) = O(n)

def isAnagram(str1, str2):
    #check for null values
    if (str1 is None) or (str2 is None):
        return "One or more missing strings"

    #check length
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False
    else:
        string1, string2 = list(str1), list(str2)

        dict = {}
#        print(string1==string2, 'Yes')
        for x in string1:
            if x in dict:
                dict[x] += 1
            else:
                dict[x] = 1

        for x in string2:
            if x in dict:
                dict[x] -= 1
            #else:
                #return False

        for x in dict.values():
            if x!=0:
                return False
        return True






print(isAnagram("public relatiOns$", "$crap built on lies"))
print(isAnagram("clint eastwood", "old west action"))
print(isAnagram("start here", "t00 action"))
print(isAnagram("clint eastwood wood", "old west action cxod"))
print(isAnagram("public relations", None))
print(isAnagram("start here rrrr", "start here eeee"))
print(isAnagram("start here tx", "start here yy"))
