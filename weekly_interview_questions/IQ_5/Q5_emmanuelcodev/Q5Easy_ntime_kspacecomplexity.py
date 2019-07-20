    '''
    Time complexity O(N)- 1 for loop
    Space complexity O(N) - 1 array of N size, to copy elements of input_array to.


    '''


def reverse_elements(array_input):
    if not array_input:
        raise Exception('array_input cannot be of NoneType or an empty list')

    reversed_array = []
    size = len(array_input)-1
    #put elements from end of list to first of new list
    for x in range(size, -1, -1):
        reversed_array.append(array_input[x])
    return reversed_array


def reverse_elements2(array_input):
    if not array_input:
        raise Exception('array_input cannot be of NoneType or an empty list')
    reversed_array = []
    #put elements from end of list to first of new list
    for x in range(len(array_input)):
        reversed_array.append(array_input.pop())
    return reversed_array


def reverse_elements3(array_input):
    if not array_input:
        raise Exception('array_input cannot be of NoneType or an empty list')
    return array_input[::-1]


print(reverse_elements([5,6,9,2]))
print(reverse_elements([-3,4]))
print(reverse_elements([0]))
print(reverse_elements([]))
print(reverse_elements(None))
