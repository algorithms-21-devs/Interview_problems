def anagram_check2(str1, str2):
    #check for Null Entries
    if str1 is None or str2 is None:#raises an exception is None is passed
        raise Exception('str1 and str2 cannot be NoneType')

    #get rid of whitespaces
    str1 = str1.replace(" ", "") #returns copy so space complexity is O(n), Time Complexity O(n)
    str2 = str2.replace(" ", "") #returns copy so space complexity is O(n), Time Complexity O(n)

    #check Lenght,return False if not equal:
    if len(str1)!=len(str2):
        return False

    #convert to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    #create dic,
    str1_dic = {}
    str2_dic = {}

    #traverse strings,save letter occurances on two independent dictionaries

    for x in str1:#O(n) for traverse
        if x in str1_dic:#if already occured in dict
            str1_dic[x]+=1
        else:
            str1_dic[x]=1 #else add it


    for x in str2:#O(n) for traverse
        if x in str2_dic:
            str2_dic[x]+=1
        else:
            str2_dic[x]=1


    '''
        The run time is O(n). It comes from iterating the original list.
        This line ---> if x not in str2_dic or str1_dic[x]!=str2_dic[x]:#
        Iterates through a dictionary so its only O(1) so the entire process
        still only takes O(n).
    '''
    #check to make sure letter occured in both dictionaries
    #then check if occurance same amount of times
    for x in str1_dic:#O(n) b/c traversing
        if x not in str2_dic or str1_dic[x]!=str2_dic[x]:#
            return False
    return True #meaning all letters oc

#except (RuntimeError, TypeError, NameError):

print(anagram_check2("public relatiOns$", "$crap built on lies"))
print(anagram_check2("clint eastwood", "old west action"))
print(anagram_check2("start here", "t00 action"))
print(anagram_check2("clzint eastwood wood", "old west action cxod"))
print(anagram_check2("start here rrrr", "start here eeee"))
print(anagram_check2("start here tx", "start here yy"))
print(anagram_check2("start here", "start here"))
print(anagram_check2("public relations", None))
