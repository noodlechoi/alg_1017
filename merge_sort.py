import random

random.seed('class_01')

array = [random.randrange(100) for _ in range(30)]
l_arr = len(array)
print(array, l_arr)

def mergeSort(arr, beg, end):   # end = inclusive
    first_rights = (beg + end + 1) // 2
    mergeSort(arr, beg, first_rights - 1)
    mergeSort(arr, first_rights, end)
    merge()

mergeSort(array, 0, l_arr - 1)