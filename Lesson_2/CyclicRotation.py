# Cyclic rotation of an array 


def solution(A, K):
    if len(A) == 0:  # if empty array
        return A  # return empty array
    if K == 0:  # if K = 0, number of cycles is 0, return the original array (A).
        return A  # return A
    if K > len(A):  # if K is bigger than length of A
        K = K % len(A)  # K is the remainder of dividing K(No of cycles) by the length of A(array)
    print(A[-K:])
    print(A[:-K])
    return A[-K:] + A[:-K]  # return last K elements + first K elements


solution([1, 2, 3, 4, 5], 1) # [5,1,2,3,4]