import node as n

class SingleLinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_start(self, data):
        if data is None:
            raise Exception('data cannot be of NoneType')

        if self.size == 0:
            self.head = n.Node(data)
            self.tail = self.head
            self.size+=1
        else:
            new_node = n.Node(data)
            new_node.next = self.head
            self.head = new_node
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
            self.tail = self.tail.next
            self.size+=1

    def delete_start(self):#Time complexity O(n)
        if self.size == 0:
            raise Exception('Cannot delete any elements due to size of list being 0')
        if self.size == 1:
            self.head = None
            self.size-=1
        else:#size > 1 (2,n)
            current_node = self.head#keeps track of old node
            self.head = self.head.next#move pointer to right
            current_node.next = None# no longer points to list
            self.size-=1


    def delete_end(self):#Time complexity O(n)
        if self.size == 0:
            raise Exception('Cannot delete any elements due to size of list being 0')
        if self.size == 1:
            self.head = None
            self.size-=1
        else:#size > 1 (2,n)
            current_node = self.head
            while current_node.next.next is not None:#until we reach 2nd to last element
                current_node = current_node.next
            current_node.next = None
            self.tail = current_node
            self.size-=1
    def traverse(self):
        if self.size == 0:
            raise Exception('No elements in the list')

        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
'''
Pleast note delete_node(self, data) is missing and will need to be added later on. It requires the first node carrying data be removed from the list
- Emmanuelcodev

'''
