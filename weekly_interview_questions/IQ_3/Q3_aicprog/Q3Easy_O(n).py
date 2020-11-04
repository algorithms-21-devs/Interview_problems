# Given a linked list, determine if that linked list is a palindrome.
#Iteration over linkedList will result in an O(N) time complexity

'''
Using a modified implemenation of DoubleLinkedList, you can insert arrays and convert them into a LinkedList.
Once you do so, you iterate over the list n/2 times while tracking the front part of the LinkedList as well as the tail part
of the LinkedList, comparing the first and last letters, then the second and second to last letters. If this comparison fails,
the algorithm returns false.

'''


#LinkedList implementation

class Node(object):

    def __init__(self, data):
        self.data = data
        self.nextNode = None
        self.previousNode = None


    def getData(self):
            return self.data

    def getNextNode(self):
            return self.nextNode
    def getPreviousNode(self):
            return self.previousNode

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertStart(self, data):
        newNode = Node(data)

        if not self.head:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            self.head.previousNode = newNode
            newNode.nextNode = self.head
            self.head = newNode
            self.size += 1

    def insertArrayAtEnd(self, str):
            for x in str:
                self.insertEnd(x)


    def insertEnd(self, data):

        newNode = Node(data)

        if not self.head:
            self.head = newNode
            self.tail = newNode
            self.size = 1
        else:
            self.tail.nextNode = newNode
            newNode.previousNode = self.tail
            self.tail = newNode

    def remove(self, data):
        if not self.head:
            return "LinkedList is empty"
        elif self.head.data == data:
            self.head = self.head.nextNode
        elif self.tail.data == data:
            self.tail = self.tail.previousNode
            self.tail.nextNode = None
        else:
            actualNode = self.head.nextNode
            while actualNode is not None:
                if actualNode.data == data:
                    actualNode.nextNode.previousNode = actualNode.previousNode
                    actualNode.previousNode.nextNode = actualNode.nextNode
                    self.size -= 1

                actualNode = actualNode.nextNode

    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print(actualNode.data)
            actualNode = actualNode.nextNode

    #additional functions
    def getSize(self):
        return self.size

    def getHead(self):
        return self.head

    def getTail(self):
        return self.tail

def isPalindrome(linkedList):
    if linkedList is None:
        raise Exception('LinkedList cannot be of NoneType')

    if linkedList.size == 0:
        raise Exception('LinkedList is an empty')


    #O(1)
    leftNode = linkedList.getHead()
    rightNode = linkedList.getTail()
    size = linkedList.getSize() / 2
    count = 0

    # At most, O(N)
    while leftNode is not None:
        #print(leftNode.getData().lower(), rightNode.getData().lower())
        if leftNode.getData().lower() != rightNode.getData().lower():
            return False

        leftNode = leftNode.getNextNode()
        rightNode = rightNode.getPreviousNode()

        count += 1

        if count == size:
            break

    return True


linkedList = LinkedList();
linkedList.insertArrayAtEnd("ana")
print(isPalindrome(linkedList))
#returns True

linkedList = LinkedList();
linkedList.insertArrayAtEnd("Ana")
print(isPalindrome(linkedList))
#returns True

linkedList = LinkedList();
linkedList.insertArrayAtEnd("peep")
print(isPalindrome(linkedList))
#returns True

linkedList = LinkedList();
linkedList.insertArrayAtEnd("rotator")
print(isPalindrome(linkedList))
#returns True

linkedList = LinkedList();
linkedList.insertArrayAtEnd("z")
print(isPalindrome(linkedList))
#returns True

linkedList = LinkedList();
linkedList.insertArrayAtEnd("hello")
print(isPalindrome(linkedList))
#returns False

linkedList = LinkedList();
linkedList.insertArrayAtEnd("james")
print(isPalindrome(linkedList))
#returns False

linkedList = LinkedList();
linkedList.insertArrayAtEnd("")
print(isPalindrome(linkedList))
#returns Exception

linkedList = LinkedList();
linkedList.insertArrayAtEnd(None)
print(isPalindrome(linkedList))
#returns Exception
