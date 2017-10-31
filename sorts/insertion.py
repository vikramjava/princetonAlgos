
__author__ = "Vikram Java"

import operator

def Insertion(input_arr, compare=operator.lt):
    for i in range(1, len(input_arr)):
        j = i - 1
        while compare(input_arr[i], input_arr[j]) and j >= 0:
            input_arr[i], input_arr[j] = input_arr[j], input_arr[i]
            j -= 1
            i -= 1
    return input_arr

if __name__ == "__main__":
    int_list = [565, 9489, 5, 55, 27, -2, 17, 1000, 17, 666]
    str_list = ['xyz', 'abc', 'rwq', 'rwa']
    Insertion(int_list)
    print int_list
    Insertion(str_list)
    print str_list