import random

random.seed('class_01')

array = [random.randrange(100) for _ in range(30)]
l_arr = len(array)
print(array, l_arr)

def merge(arr, first_left, first_right, end):  #end = inclusive
    merged = []
    l, r = first_left, first_right
    # 두 그룹에 선수가 있으면
    while A반에 선수 있다 and B반에 선수 있다:
        # 진 선수는 가서 줄 서 있어
        if A반 선수가 졌어 or 비겼어:
            A반 선수 줄 서 있어
        else:
            B반 선수 줄 서 있어
    while A반에 선수 있다:
        남은 선수추가
    while B반에 선수 있다:
        남은 선수추가
    merged에 있는 것을 arr로 옮기기
    
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