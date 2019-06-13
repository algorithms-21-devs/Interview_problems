#Question
#Given two strings, check to see if they are anagrams. An anagram is when the two strings can be written
#using the exact same letters (so you can just rearrange the letters to get a different phrase or word).
#consider characters only to be lowercase only a-z
#Test Cases:
#"public relations" is an anagram of "crap built on lies."
#"clint eastwood" is an anagram of "old west action"



def anagram_check(str1, str2):#Time complexity O(n)
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "") #remove empty spaces

    if len(str1)!=len(str2): #O(n) at max
        return False
    str1_alpha_tracker = [0 for x in range(26)]#keeps track of quantitiy of letters in the alphabet for original string, 0 = a, b =1 , c = 3, d = 4
    str2_alpha_tracker = [0 for x in range(26)]#keeps track of quantitiy of letters in the alphabet


    for x in str1:#Time complexity O(n), lenght of string1
         str1_alpha_tracker[97 - ord(x)] #97 is a, subtract ascii value to find what position in the array to incremement

    for x in str2:#Time complexity O(n), lenght of string2
         str2_alpha_tracker[97 - ord(x)]

    for x in range(26):
        if str2_alpha_tracker[x] != str1_alpha_tracker[x]:#compare number of a's, b's ... z's of each string.
            return False
    return True



print(anagram_check("public relations", "crap built on lies"))
print(anagram_check("clint eastwood", "old west action"))
print(anagram_check("ce", "old west action"))
