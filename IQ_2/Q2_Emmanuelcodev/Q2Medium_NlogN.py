'''
    The following algorithm unique_pairs takes O(nlogn) time complexity
    3 different algorithms are used in total.

    1) unique_pairs takes n logn time
    2) binary_search takes log n time
    3) remove_duplicates takes nLogn time


    unique_pairs
        -->1) tim sorts the list at a O(nlogn) cost.
           : Total time complexity so far = O(nlogn)
        -->2)iterates through the sorted list with O(N) time complexity,
           2a)finds the compliment of the current number that would equal the target_sum
           2b)Performs binary_search to see if compliment in in list at Log(N) time.
              Since binary_search is nested in n iteration, it is in nLogn time complexity.
              If the compliment is in the list, it is appends the pair in a new list.
            : Total time complexity so far = O(nlogn) + O(nlogn)
        --->3)remove_duplicates is called to get rid of duplicate pairs, it sorts and remove_duplicates in O(nlogn) time
            : Total time complexity so far = O(nlogn) + O(nlogn) + O(nlogn) =  O(nlogn)



'''
def unique_pairs(int_list, target_sum):
    #check for None
    if None in (int_list, target_sum):
        raise Exception("int_list and target_sum cannot be of NoneType")

    if len(int_list) < 1:
        return []

    #int_list = remove_duplicates(int_list)#nlogn time b/c remove_duplicates tim sorts with O(nlogn)
    int_list = sorted(int_list)#nlogn
    pairs = []
    #print(int_list)
    for x in range(len(int_list)):#interate through entire list
        compliment = target_sum - int_list[x]
        result = binary_search(int_list, 0, len(int_list)-1, compliment)#find compliment, and then do binary search to find it in the list
        #print('compliment is ', compliment)
        #print(result)
        if result[0]:#if compliment is found
            if result[1] == x: #cannot count a pair i.e. (1,1) if the compliment being used is the same exact position in the array as current num b/c its counting it as a seperate number
                pass
            else:
                if int_list[x] < compliment:
                    pairs.append((int_list[x], compliment))
                else:
                    pairs.append((compliment, int_list[x]))

    if len(pairs) > 1:
        return remove_duplicates(pairs)#time sort in nlogn at worst, n at best
    return pairs




#This binary search algorithm is not mine entirely, I modified it , the other two algoritms aremine entirely. Credit to the orgiinal binary search goes to https://www.geeksforgeeks.org/binary-search/
def binary_search(arr, left_index, right_index, target_num):

    while left_index <= right_index:

        mid = left_index + (right_index- left_index)//2;

        # Check if x is present at mid
        if arr[mid] == target_num:
            return (True, mid)

        # If x is greater, ignore left half
        elif arr[mid] < target_num:
            left_index = mid + 1

        # If x is smaller, ignore right half
        else:
            right_index = mid - 1

    # If we reach here, then the element
    # was not present
    return (False,-1)


#binarySearch(arr, 0, len(arr)-1, x)
def remove_duplicates(list_ints):
    list_ints = sorted(list_ints)#nlogn
    #print('sorted list_ints is',  list_ints)

    prev_element = list_ints[0]
    no_duplicates = [prev_element]

    for x in list_ints:#O(n) time
        if x == prev_element:
            pass
        else:
            no_duplicates.append(x)
            prev_element = x
    return no_duplicates


print(unique_pairs([1, 3, 2, 2,3,5,5], 4))  # Returns [(3,1),(2,2)]

print(unique_pairs([3, 4, 19, 3, 4, 8, 5, 5], 6))#returns 3,3
print(unique_pairs([-1, 6, -3, 5, 3, 1], 2))  # Returns [(-1,3),(5,-3)]
print(unique_pairs([3, 4, 19, 3, 3, 3, 3], 6))  # Returns [(3,3)]
print(unique_pairs([-1, 6, -3, 5, 3, 1], 5000))  # Returns []
print(unique_pairs([], 10))  # Returns []
print(unique_pairs([4],54)) #returns []
print(unique_pairs(None,54))# raises Exception
