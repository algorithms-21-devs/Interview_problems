# Function to reverse A[] from start to end
def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1




#
'''
This program is contributed by Pratik Chhajer
Credit goes to : https://www.geeksforgeeks.org/write-a-program-to-reverse-an-array-or-string/
'''
