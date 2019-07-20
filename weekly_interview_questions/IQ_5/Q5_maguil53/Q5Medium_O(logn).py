# Time Complexity: O(ln)
def reverseIntArray(int_list):
    if int_list is None:
        raise Exception("Can't enter None")

    length = len(int_list)

    if length == 0:
        return None

    half = length // 2

    for i in range(half):
        temp = int_list[i]
        # Swap element on left with one on the right
        int_list[i] = int_list[length - 1 - i]
        # Swap element on right with one on the left
        int_list[length - 1 - i] = temp

    return int_list


print(reverseIntArray([5, 6, 9, 2]))
print(reverseIntArray([-3, 4]))
print(reverseIntArray([0]))
print(reverseIntArray([]))
print(reverseIntArray(None))
