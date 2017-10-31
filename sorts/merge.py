
__author__ = "Vikram Java"

import operator

def merge(input_arr, aux_arr, low, mid, high):

    for k in range(low, high+1):
        aux_arr[k] = input_arr[k]

    i = low
    j = mid + 1

    for k in range(low, high + 1):
        if (i > mid):
            input_arr[k] = aux_arr[j]
            j += 1
        elif (j > high):
            input_arr[k] = aux_arr[i]
            i += 1
        elif (operator.lt(aux_arr[j], aux_arr[i])):
            input_arr[k] = aux_arr[j]
            j += 1
        else:
            input_arr[k] = aux_arr[i]
            i += 1

def _sort(i_arr, aux, lo, high):
    if high <= lo:
        return

    mid = lo + (high - lo)/2

    _sort(i_arr, aux, lo, mid)
    _sort(i_arr, aux, mid+1, high)
    merge(i_arr, aux, lo, mid, high)


def Sort(input_arr):
    aux = [None for _ in range(len(input_arr))]
    _sort(input_arr, aux, 0, len(input_arr) - 1)

if __name__ == "__main__":
    int_list = [565, 9489, 5, 55, 27, -2, 17, 1000, 17, 666]
    str_list = ['xyz', 'abc', 'rwq', 'rwa']
    Sort(int_list)
    print int_list
    Sort(str_list)
    print str_list