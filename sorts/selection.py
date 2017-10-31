__author__ = "Vikram Java"

import operator

def Selection(input_arr, compare=operator.lt):
    for i in range(0, len(input_arr)):
        min_index = i
        for j in range(i, len(input_arr)):
            if compare(input_arr[j], input_arr[min_index]):
                min_index = j

        input_arr[min_index], input_arr[i] = input_arr[i], input_arr[min_index]

if __name__ == "__main__":
    int_list = [565, 9489, 5, 55, 27, -2, 17, 1000, 17, 666]
    str_list = ['xyz', 'abc', 'rwq', 'rwa']
    Selection(int_list)
    print int_list
    Selection(str_list)
    print str_list
