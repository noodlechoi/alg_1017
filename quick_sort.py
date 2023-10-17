import random

random.seed('class_01')

array = [random.randrange(100) for _ in range(30)]
l_arr = len(array)
print(array, l_arr)
