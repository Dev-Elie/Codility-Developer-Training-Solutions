# Array =[1, 2, 3, 5]
# Index = 0, 1, 2, 3

# Algorithm will check for each element in the array, if it's equal to the index of the element + 1
# when it reaches a point where the pattern breaks, it will return the missing element

def solution(A):
    if len(A) == 0: # If the array is empty, return 1
        return 1
    A.sort() # Sort the array
    for i in range(len(A)): # For each element in the array
        if A[i] != i+1: # If the element is not equal to the index of the element + 1
            return i+1 # Return the index of the element + 1
    return len(A)+1 # If the array is full, return the length of the array + 1

solution([1, 2, 3, 5])