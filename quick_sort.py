import random

# random.seed('class_01')

array = [random.randrange(100) for _ in range(30)]
l_arr = len(array)
print(array, l_arr)

def partition(arr, beg, end): #end = exclusive
    # randint는 끝 포함
    ri = random.randrange(beg, end)
    arr[beg], arr[ri]= arr[ri], arr[beg]

    # 아래에서는 맨 왼쪽의 값을 피벗으로
    pv = arr[beg]

    p, q = beg + 1, end - 1
    while True: # 역전 안됐으면:
        while True:
            # if p >= end: break
            if p >= q: break
            if arr[p] > pv: break
            # p 증가
            p += 1
        while True:
            # 같으면 피벗이 q가 아니게 됨
            if p > q: break
            if arr[q] <= pv: break
            # q 감소
            q -= 1
        if p >= q: break
        # p / q swap
        arr[p], arr[q] = arr[q], arr[p]
        p += 1
        q -= 1

    arr[q], arr[beg] = arr[beg],arr[q]
    return q

def quickSort(arr, beg, end): #end = exclusive
    size = end - beg
    if size <= 1: return
    pivot = partition(arr, beg, end)
    quickSort(arr, beg, pivot)
    quickSort(arr, pivot + 1, end)

quickSort(array, 0, l_arr)
print(array)