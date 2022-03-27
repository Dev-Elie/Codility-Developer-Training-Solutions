# binary gap solution
def binaryGap(N):
    binary = bin(N)  # convert to binary --> '0b100'
    binary = binary[2:]  # remove '0b' from the beginning
    binary = binary.split("1")  # split the binary string into a list of strings
    binary = list(filter(None, binary))  # remove empty strings from the list
    binary = list(map(len, binary))  # convert each string to an integer
    if len(binary) == 0:  # if the list is empty
        return 0  # return 0
    else:  # if the list is not empty
        return max(binary)  # return the maximum value in the list

output = binaryGap(1041) 
print(output)
