# frog jump

# X = starting point
# Y = ending point
# D = jump distance


def solution(X, Y, D):
    # write your code in Python 3.6
    if X == Y:  # if X and Y are equal, return 0
        return 0

    if X < Y:  # if X is less than Y, calculate the number of jumps needed
        # here we apply the floor division operator to ensure integer division, normal division would return a float
        return (Y - X) // D + 1  # +1 because we need to jump to the end
    else:
        return -1  # if X is greater than Y, return -1
