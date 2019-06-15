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
    #check length
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    if len(str1) != len(str2):
        return False
    else:
        string1, string2 = list(str1), list(str2)

        dict = {}

        for x in string1:
            dict[x] = 0


        for x in string2:
            if x not in dict:
                return False

        return True


        #return all(dic.keys())


print(isAnagram("public relations", "crap built on lies"))
print(isAnagram("clint eastwood", "old west action"))
print(isAnagram("cekjdfjlsdfdd", "old west action"))
