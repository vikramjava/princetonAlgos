
__author__ = "Vikram Java"

import random
import operator
less = operator.lt


def partition(input_array, lo, hi):
    i = lo
    j = hi + 1


    while True:

        i += 1
        while(less(input_array[i], input_array[lo])):
            if (i == hi):
                break
            i += 1

        j -= 1
        while(less(input_array[lo], input_array[j])):
            if (j == lo):
                break
            j -= 1

        if (i >= j):
            break

        input_array[i], input_array[j] = input_array[j], input_array[i]

    input_array[lo], input_array[j] = input_array[j], input_array[lo]
    return j

def _sort(in_arr, lo, hi):
    if hi <= lo:
        return

    x = partition(in_arr, lo, hi)
    _sort(in_arr, lo, x-1)
    _sort(in_arr, x+1, hi)

def Quick(input_array):
    random.shuffle(input_array)
    _sort(input_array, 0, len(input_array)-1)

if __name__ == "__main__":
    int_list = [565, 9489, 5, 55, 27, -2, 17, 1000, 17, 666]
    str_list = ['xyz', 'abc', 'rwq', 'rwa']
    Quick(int_list)
    print int_list
    Quick(str_list)
    print str_list
