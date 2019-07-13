import single_linked_list as sll

def rotate_by_2(l_list):

    if l_list is None:
        raise Exception('l_list cannot be of NoneType')

    if l_list.size == 0:
        raise Exception('l_list cannot be of NoneType')
    elif l_list.size <=2:
        return l_list
    else:
        current_node = l_list.head
        temp_node = None #will hold the last two elements of the linked_list before the rotation

        while current_node.next.next.next is not None:#stops at 3rd to last element, these will be moved to the top of the list hence leaving us with a rotation of two
            current_node = current_node.next

        temp_node = current_node.next#now points to two last elements
        current_node.next = None#disconnects last two elements, so linked list has lost two elements

        temp_node.next.next = l_list.head#so last two elements now point to head, so they are first
        l_list.head = temp_node#head points now to very top element again.



#testing algorithm
sample1 = sll.SingleLinkedList()
sample1.insert_end(1)
sample1.insert_end(2)
sample1.insert_end(3)
sample1.insert_end(4)
sample1.insert_end(5)


sample2 = sll.SingleLinkedList()
sample2.insert_end(1)
sample2.insert_end(2)
sample2.insert_end(3)
sample2.insert_end(4)
sample2.insert_end(5)
sample2.insert_end(6)



sample3 = sll.SingleLinkedList()
sample3.insert_end(1)


sample4 = sll.SingleLinkedList()
sample4.insert_end(1)
sample4.insert_end(2)


rotate_by_2(sample1)
print(sample1.traverse(), '\n')#should return 5,4,1,2,3, since original is 1,2,3,4,5
rotate_by_2(sample2)
print(sample2.traverse(), '\n')#should return 5,6,1,2,3,4 since original is 1,2,3,4,5,6
rotate_by_2(sample3)
print(sample3.traverse(), '\n')#should return 1 since original is 1
rotate_by_2(sample4)
print(sample4.traverse(), '\n')#should return 1,2 since original 1,2
