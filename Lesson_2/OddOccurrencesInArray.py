# Odd Occurrences In an Array

def solution(A): 
    A.sort() # sort the array
    A.append(-1) # add -1 to the end of the array, so that we don't exceed the length of the array
    for i in range(0,len(A),2): # loop through the array, starting at 0, increment by 2 till the end of the array
        if A[i] != A[i+1]: # if the current element is not equal to the next element
            return A[i] # return the current element

output = solution([9,3,9,3,9,7,9]) # 7
print(output) # 7
