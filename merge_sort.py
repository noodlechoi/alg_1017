import random

# random.seed('class_01')

array = [random.randrange(100) for _ in range(30)]
l_arr = len(array)
print(array, l_arr)

def merge(arr, first_left, first_right, end):  #end = inclusive
    merged = []
    l, r = first_left, first_right
    # 두 그룹에 선수가 있으면
    while l < first_right and r <= end: # A반에 선수 있다 and B반에 선수 있다:
        # 진 선수는 가서 줄 서 있어
        # 포함 : stable하게 만들기 위해
        if arr[l] <= arr[r]: #A반 선수가 졌어 or 비겼어:
            # A반 선수 줄 서 있어
            merged.append(arr[l])
            l += 1
        else:
            # B반 선수 줄 서 있어
            merged.append(arr[r])
            r += 1
    # 아래 두 루프 중 하나만 돌 것이다
    # while l < first_right: # A반에 선수 있다:
    #     # 남은 선수추가
    #     merged.append(arr[l])
    #     l += 1
    # while r <= end: # B반에 선수 있다:
    #     # 남은 선수추가
    #     merged.append(arr[r])
    #     r += 1
    if l < first_right:# A반에 선수가 있다
        merged += arr[l:first_right]
        arr[first_left:end + 1] = merged
    else:
        # merged += arr[r:end + 1]
        arr[first_left:r] = merged
    # merged에 있는 것을 arr로 옮기기

def mergeSort(arr, beg, end):   # end = inclusive
    # size = end - beg + 1
    # if size <= 1: return
    if beg >= end: return
    first_right = (beg + end + 1) // 2
    mergeSort(arr, beg, first_right - 1)
    mergeSort(arr, first_right, end)
    merge(arr, beg, first_right, end)


mergeSort(array, 0, l_arr - 1)
print(array)