'''
Given an integer array, output all the unique pairs that sum up to a specific value K.

Time: O(n) from iterating over list array

'''

def uniquePairsOfK(list, k):
    #Find counterpart and put them in dictionary
    duplicates = {}
    counterparts = {}
    uniquePairs = []

    count = 0
    if None in (list, k):
        raise Exception("Either your list, or value for k is empty")

    if len(list) < 2:
        return []


    # iterate through list finding the counterpart (k - num) of every number in the list
    for num in list:

        counterpart = k - num

        # to avoid to duplicate entries, it always enters counterparts based on (smaller #, (bigger #, which # is bigger, index)
        if num < counterpart:
            counterparts[num] = (counterpart, 2, count)
        else:
            counterparts[counterpart] = (num, 1, count)
        count += 1

        # dictionary to keep track of duplicates
        if num in duplicates:
            duplicates[num] += True
        else:
            duplicates[num] = False

    # Iterates over counterparts. If
    for (x, y) in counterparts.items():
        # case 1: counterpart is smaller
        if y[1] == 2:
            #checks if the counterpart is in duplicates, which includes the original list as its keys
            if y[0] in duplicates.keys() and (x + y[0] == k):
                # checks to see that if counterparts are the same, it is not counting the same number if they are not duplicates
                  if x == y[0] and (not duplicates[y[0]]):
                      continue
                  else:
                      #else it adds it to the list
                      uniquePairs.append((x, y[0]))
        #case 2: counterpart is bigger and the same process is repeated but checks for x instead
        else:
            if x in duplicates.keys() and (x + y[0] == k):
                  if x == y[0] and (not duplicates[x]):
                      continue
                  else:
                      uniquePairs.append((x, y[0]))

    print(uniquePairs)



uniquePairsOfK([1, 3, 2, 2, 3, 1, 3, 2, 2, 1, 3,3,1], 4)
uniquePairsOfK([1,3, 4, 0, 2, 2, 5],4) #returns [(2,2),(1,3)]
uniquePairsOfK([-1,6,-3,5, 3,1], 2)  #returns [(-1,3),(5,-3) ]
uniquePairsOfK([-1,6,-3,5, 3,1], 5000) #returns returns [], None, Null,or -1 depending on your language
uniquePairsOfK([3, 4, 19, 3, 3, 3, 3], -6)
uniquePairsOfK([-1,6,-3,5, 3,1, 3, 1, 1, 3], 2)
uniquePairsOfK([],10) #returns Exception
uniquePairsOfK(None, 10)
