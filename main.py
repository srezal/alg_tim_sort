def calculate_minrun(n):
    r = 0
    while n >= 64:
        r |= n & 1
        n >>= 1
    return n + r


def get_run(arr, n, ptr, minrun):
    if ptr == n - 1:
        return ptr + 1, True
    is_increasing = arr[ptr + 1] > arr[ptr]
    cnt = 1
    while (ptr + cnt + 1 < n):
        if arr[ptr + cnt] < arr[ptr + cnt + 1] and not is_increasing:
                return ptr + cnt + min(minrun - cnt, n - (ptr + cnt)), False
        elif arr[ptr + cnt] > arr[ptr + cnt + 1] and is_increasing:
                return ptr + cnt + min(minrun - cnt, n - (ptr + cnt)), True
        cnt += 1
    return ptr + cnt + min(minrun - cnt, n - (ptr + cnt)), is_increasing


def MERGE(arr1, arr2):
    i = 0
    j = 0
    result = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result += arr1[i:] + arr2[j:]
    return result


def InsertionSort(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            if i == 1:
                arr.insert(0, arr.pop(i))
            for j in range(i - 2, -1, -1):
                if arr[j] < arr[i]:
                    arr.insert(j + 1, arr.pop(i))
                    break
                elif j == 0:
                    arr.insert(0, arr.pop(i))
    return arr


def tim_sort(arr, n):
    minrun = calculate_minrun(n)
    if n <= 63:
        return InsertionSort(arr)
    ptr = 0
    runs = []
    while ptr < n:
        run_end_ptr, is_increasing = get_run(arr, n, ptr, minrun)
        if not is_increasing:
            runs.append(InsertionSort(arr[ptr:run_end_ptr][::-1]))
        else:
            runs.append(InsertionSort(arr[ptr: run_end_ptr]))
        ptr = run_end_ptr
    while len(runs) > 1:
        runs.append(MERGE(runs.pop(0), runs.pop(0)))
    return runs[0]

    

def check_is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            return False
    return True


import random
import time

N = 1000

arr = [random.randint(0, 1000) for _ in range(1000000)]
#print(arr)
my_start_time = time.time()
sorted_arr = tim_sort(arr, len(arr))
my_stop_time = time.time()
#print(sorted_arr)
start_time = time.time()
sorted(arr)
stop_time = time.time()
print('my tim_sort:', my_stop_time - my_start_time)
print('python tim_sort:', stop_time - start_time)
print(check_is_sorted(sorted_arr))