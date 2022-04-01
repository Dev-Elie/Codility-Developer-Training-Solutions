# # Comparison of different time complexities
# # 1) Linear time — O(n).


# def get_squared_numbers(numbers):
#     squared_numbers = []
#     # Time taken for execution will depend on the size of the array.
#     # For the case of an array of 4m, the program will need to do 4M iterations
#     # The time taken is equally propotional to the number of computation it's doing, therefore
#     # the time will grow linearly
#     for n in numbers:
#         squared_numbers.append(n * n)
#     return squared_numbers


# numbers = [1, 2, 3, 4, 5]
# get_squared_numbers(numbers)  # [1, 4, 9, 16, 25]


# # 2) Constant time — O(1).

# # Here the time execution will remain the same regardless.

# def find_first_pe(prices, eps, index):
#     pe = prices[index]/eps[index]
#     return pe

# # 3) Quadratic time — O(n2).

# def find_duplicate():
#     numbers = [3,6,2,4,3,6,8,9]
#     for i in range(len(numbers)):
#         for j in range(i+1, len(numbers)):
#             if numbers[i] == numbers[j]:
#                 print(numbers[i] + "is a duplicate")
#                 break
    

