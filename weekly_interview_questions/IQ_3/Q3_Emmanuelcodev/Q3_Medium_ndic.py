import single_linked_list as sll

sample1 = sll.SingleLinkedList()
sample1.insert_end('A')
sample1.insert_end('N')
sample1.insert_end('A')

sample2 = sll.SingleLinkedList()
sample2.insert_end('A')
sample2.insert_end('N')
sample2.insert_end('a')


sample3 = sll.SingleLinkedList()
sample3.insert_end('p')
sample3.insert_end('e')
sample3.insert_end('e')
sample3.insert_end('p')

sample4 = sll.SingleLinkedList()
sample4.insert_end('r')
sample4.insert_end('o')
sample4.insert_end('t')
sample4.insert_end('a')
sample4.insert_end('t')
sample4.insert_end('o')
sample4.insert_end('r')

sample5 = sll.SingleLinkedList()
sample5.insert_end('z')

sample6 = sll.SingleLinkedList()
sample6.insert_end('h')
sample6.insert_end('e')
sample6.insert_end('l')
sample6.insert_end('l')
sample6.insert_end('o')

sample7 = sll.SingleLinkedList()
sample7.insert_end('j')
sample7.insert_end('a')
sample7.insert_end('m')
sample7.insert_end('e')

sample8 = sll.SingleLinkedList()


def is_palindrome(s_linked_list):

    '''
    Explanation of Algorithm:
    1) idea is to image the linked list as array split down the middle
    2) Imagine being at the middle of the list and from the middle position reading the left part of the list from right to left, and from the middle position reading the right part of the list from left to right
    3) if both sides are equal when we read it this way then it has to be a palindrome
    4) To read it like this we use position
    5) we first create two dictionaries to track the letters that appear in each half and the position of those letters that occur in each half of the list.
    6) Position for left side of list, it starts at n, then n-1, then n-1, all the way to last element whose position we count as 0
    7) Position for right side, it starts at 0, then 0 + 1, then 0 + 1 + 1, all the way the last element # NOTE:
    8) We store the letter as the key and position of the occurance of each letter as the value
    9) if we compare both dictionaries and they are the same, meaning both sides of the list are equal then we return True to palindrome

    Time complexity is O(n) since it is all done through one iteration of the list
    We check the dictionary which at most is O(n), one for each letter.
    In the worse case where it is all one letter, the dictionary would compare 1 element n times agaist the second dictionary
    This is O(n)

    '''
    if s_linked_list is None:
        raise Exception('s_linked_list cannot be of NoneType')

    if s_linked_list.size == 0:
        raise Exception('s_linked_list is an empty linked list')



    current_node = s_linked_list.head
    #determine size of list
    size = s_linked_list.size
    half_size = size // 2# we will iterate through the linked list , one half at a time
    left_half_position = half_size-1#used to indicate position of elements, -1 b/c of index starts at 0

    #determine if list is even or odd
    odd = False #assume it's even
    if size % 2 != 0:#change if it's odd
        odd = True


    left_letter_positions = {}
    counter = 0
    #go through half of the linked list and track element and position of element
    while counter!= half_size:
        if current_node.data in left_letter_positions:
            left_letter_positions[current_node.data.upper()].append(left_half_position)
            left_half_position-=1
        else:
            left_letter_positions[current_node.data.upper()] = [left_half_position]
            left_half_position-=1

        counter+=1
        current_node = current_node.next
    #print(left_letter_positions)
    #if odd skip middle node
    if odd:
        current_node = current_node.next
    counter = 0#counter reset at 0, since now going to travers left to right instead of right to left

    right_letter_positions = {}

    while current_node is not None:
        if current_node.data in right_letter_positions:
            right_letter_positions[current_node.data.upper()].append(counter)
        else:
            right_letter_positions[current_node.data.upper()] = [counter]
        current_node = current_node.next
        counter+=1


    for x in left_letter_positions.keys():
        if x in right_letter_positions:
            if left_letter_positions[x]==right_letter_positions[x]:#if letter occurs but at different positions
                continue
            return False
        return False#if both sides don't have the same letters, then not a palindrome
    return True
print(is_palindrome(sample1))
print(is_palindrome(sample2))
print(is_palindrome(sample3))
print(is_palindrome(sample4))
print(is_palindrome(sample5))
print(is_palindrome(sample6))
print(is_palindrome(sample7))
print(is_palindrome(sample8))
print(is_palindrome(None))
