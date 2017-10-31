
__author__ = "Vikram Java"

import operator

def Shell(input_arr, compare=operator.lt):

    h = 1
    while h < len(input_arr)/3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(1, len(input_arr), h):
            j = i - 1
            while compare(input_arr[i], input_arr[j]) and j >= 0:
                input_arr[i], input_arr[j] = input_arr[j], input_arr[i]
                j -= h
                i -= 1
        h /= 3
    return input_arr

if __name__ == "__main__":
    int_list = [565, 9489, 5, 55, 27, -2, 17, 1000, 17, 666]
    str_list = ['xyz', 'abc', 'rwq', 'rwa']
    Shell(int_list)
    print int_list
    Shell(str_list)
    print str_list