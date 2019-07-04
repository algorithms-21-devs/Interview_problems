# Time complexity: O(n)
def isLinkedPalindrome(linked_list):

    if linked_list is None:
        raise Exception("Can't enter None")

    if (linked_list.get_size() == 0):
        raise Exception("Can't enter empty list")

    # If length of linked_list is 1, return true
    if(linked_list.get_size() == 1):
        return True

    # linked_list length is greater than 1
    current = linked_list.headval
    stack = []
    half = linked_list.get_size() // 2
    listIsOdd = half % 2 != 0

    # If linked_list's size is 5, "half" should be 2
    # for-loop runs for "half" iterations
    for x in range(half):
        stack.append(current.dataval.lower())
        current = current.nextval

    # Skip over middle node if linked_list is odd
    if(listIsOdd):
        current = current.nextval

    for x in range(half):
        # Pop char off stack and compare with current.
        # Update current if equal, else return false
        if current.dataval == (stack.pop()).lower():
            current = current.nextval
        else:
            return False

    # If we have reached this point it means we have no more things to pop
    return True


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    def __init__(self):
        self.headval = None
        self.size = 0

    # Function to add newnode
    def add(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            self.size += 1
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode
        self.size += 1

    def get_size(self):
        return self.size
# Got the classes from
# https://www.tutorialspoint.com/python/python_linked_lists.htm


list1 = SLinkedList()
list1.add('a')
list1.add('n')
list1.add('a')

list2 = SLinkedList()
list2.add('A')
list2.add('n')
list2.add('a')

list3 = SLinkedList()
list3.add('p')
list3.add('e')
list3.add('e')
list3.add('p')

list4 = SLinkedList()
list4.add('r')
list4.add('o')
list4.add('t')
list4.add('a')
list4.add('t')
list4.add('o')
list4.add('r')

list5 = SLinkedList()
list5.add('z')

list6 = SLinkedList()
list6.add('h')
list6.add('e')
list6.add('l')
list6.add('l')
list6.add('o')

list7 = SLinkedList()
list7.add('j')
list7.add('a')
list7.add('m')
list7.add('e')
list7.add('s')

empty_list = SLinkedList()

print(isLinkedPalindrome(list1))  # Returns True
print(isLinkedPalindrome(list2))  # Returns True
print(isLinkedPalindrome(list3))  # Returns True
print(isLinkedPalindrome(list4))  # Returns True
print(isLinkedPalindrome(list5))  # Returns True
print(isLinkedPalindrome(list6))  # Returns False
print(isLinkedPalindrome(list7))  # Returns False
print(isLinkedPalindrome(empty_list))  # Returns Exception
print(isLinkedPalindrome(None))  # Returns Exception
