# Time Complexity: O(n)
def findPairsOfSum(nums, sum):

    if nums is None:
        raise Exception('Invalid input for list.')

    if len(nums) < 2:
        raise Exception('Not enough values for list.')

    complements = {}
    pairs = []

    for current_num in nums:
        if(current_num < 0):
            key = (current_num * -1) + sum
        else:
            key = sum - current_num

        if key in complements:
            # Used to check if the pair has already been added to pairs list
            isKeyAlreadyPaired = complements.get(key)  # Returns True or False

            if(isKeyAlreadyPaired):
                # Need to check if current_num is in dictionary,
                # because if it isn't, that means that the key can
                # be used AGAIN with current_num to make another unique pair
                if (current_num in complements):
                    continue
                else:
                    pairs.append((current_num, key))

            else:
                pairs.append((current_num, key))
                # Value of key and current_num are set to True because they
                # have been paired with another number
                complements[key] = True
                complements[current_num] = True

        else:
            # Create new entry with current_num as the key with a value of False
            complements[current_num] = False

    return pairs


print(findPairsOfSum([1, 3, 2, 2], 4))  # Returns [(3,1),(2,2)]
print(findPairsOfSum([-1, 6, -3, 5, 3, 1], 2))  # Returns [(-1,3),(5,-3)]
print(findPairsOfSum([3, 4, 19, 3, 3, 3, 3], 6))  # Returns [(3,3)]
print(findPairsOfSum([-1, 6, -3, 5, 3, 1], 5000))  # Returns []
print(findPairsOfSum([], 10))  # Returns Exception
print(findPairsOfSum(None, 10)) # Returns Exception
