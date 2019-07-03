# Time Complexity: O(nlogn)
def isAnagram(str1, str2):
    # Check if any are None/Null
    if(str1 is None or str2 is None):
        return False

    # Get rid of white space.
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    # Check if length are the same.
    if len(str1) != len(str2):
        return False

    """
        Since Python's sorted() is based on Timsort:
            Best Case: O(n)
            Average Case: O(nlogn)
            Worst Case: O(nlogn)
    """
    # Sort strings.
    key1 = ''.join(sorted(str1))
    key2 = ''.join(sorted(str2))

    my_dictionary = {
        key1: 1
    }

    # Attempt to retrieve key1 using key2.
    # If False is returned, then strings are not anagrams.
    keyExists = my_dictionary.get(key2, False)

    if not (keyExists):
        return False
    else:
        return True


print(isAnagram("hello", None))  # Returns False
print(isAnagram("public relations", "crap built on lies"))  # Returns True
print(isAnagram("clint eastwood", "old west action"))  # Returns True
print(isAnagram(" hello ", " hello there"))  # Returns False
print(isAnagram("start ", " starx"))  # Returns False
print(isAnagram("start", "start"))  # Returns True
print(isAnagram("jo", " job "))  # Returns False