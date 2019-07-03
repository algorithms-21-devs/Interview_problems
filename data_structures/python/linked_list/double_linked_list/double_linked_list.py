import node as n

class DoubleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_start(self, data):#Time complexity is O(1)
        if data is None:
            raise Exception('data cannot be of NoneType')

        if self.size == 0:
            self.head = n.Node(data)
            self.tail = self.head
            self.size+=1
        else:
            new_node = n.Node(data)
            new_node.next = self.head#make new node point to old head
            self.head.previous = new_node#make old head point backwards to new node

            self.head = new_node#move pointer to the left
            self.size+=1

    def insert_end(self, data):#done in O(1) time with help of tail attribute, no iteration required
        if data is None:
            raise Exception('data cannot be of NoneType')

        if self.size == 0:
            self.head = n.Node(data)
            self.tail = self.head
            self.size+=1
        else:
            self.tail.next = n.Node(data)
            self.tail.next.previous = self.tail#make new element point at old tail
            self.tail = self.tail.next#move tail 1 to right
            self.size+=1

    def delete_start(self):#Time complexity O(1)
        if self.size == 0:
            raise Exception('Cannot delete any elements due to size of list being 0')
        if self.size == 1:
            self.head = None
            self.size-=1
        else:#size > 1 (2,n)
            current_node = self.head#keeps track of old node

            self.head = self.head.next#move pointer to right
            self.head.previous = None#disconnect pointer to old head

            current_node.next = None# old head no longer points to list
            self.size-=1


    def delete_end(self):#Time complexity O(1) due to being able to access tail and iterate backwards
        if self.size == 0:
            raise Exception('Cannot delete any elements due to size of list being 0')
        if self.size == 1:
            self.head = None
            self.size = 0
        else:#size > 1 (2,n)
            current_node = self.tail.previous
            current_node.next = None#disconnect last element

            self.tail.previous = None#get rid of loose link element
            self.tail = current_node
            self.size-=1

    def traverse(self):#Time complexity is O(n)
        if self.size == 0:
            raise Exception('No elements in the list')

        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next


'''
Pleast note: delete_node(self, data) is missing and will need to be added later on. It requires the first node carrying data be removed from the list
- Emmanuelcodev
'''
