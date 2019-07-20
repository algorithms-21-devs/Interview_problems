def inplace_reverse(array_input):
    if not array_input:
        raise Exception('array_input cannot be of NoneType or an empty list')

    #size, iterate only through half swapping first and last element.
    '''
    Time complexity O(N)- 1 for loop
    Space complexity O(1) - 1 variable


    '''
    size = len(array_input)
    half_size = size // 2

    #swap
    for x in range(half_size):
        temp_node = array_input[0]
        array_input[x] = array_input[size-1]
        array_input[size-1] = temp_node
        size-=1
    return array_input









print(inplace_reverse([5,6,9,2]))
print(inplace_reverse([-3,4]))
print(inplace_reverse([-3,4,5]))
print(inplace_reverse([0]))
print(inplace_reverse([]))
print(inplace_reverse(None))
