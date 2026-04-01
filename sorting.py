import random 
# ------------------------------ Insertion Sort ------------------------------ #
def insertion_sort(arr):
    data = arr[:]
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# ------------------------------ Selection Sort ------------------------------ #
def selection_sort(arr):
    data = arr[:]
    n = len(data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if data[j] < data[min_idx]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data

# -------------------------------- Shell Sort -------------------------------- #
def shell_sort(arr):
    data = arr[:]
    n = len(data)

    gaps = [1]
    k = 1
    while True:
        gap = (4**k) + 3 * (2**(k - 1)) + 1
        if gap >= n:
            break
        gaps.append(int(gap))
        k += 1
    
    for gap in reversed(gaps):
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp

    return data

# --------------------------------- Heap Sort -------------------------------- #
def heapify(data, n, i):
    largest = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2

    if left_child < n and data[left_child] > data[largest]:
        largest = left_child

    if right_child < n and data[right_child] > data[largest]:
        largest = right_child

    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        heapify(data, n, largest)

def heap_sort(arr):
    data = arr[:]
    n = len(data)

    for i in range(n // 2 - 1, -1, -1):
        heapify(data, n, i)
    
    for i in range(n - 1, 0, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)
    
    return data

# ------------------------- Quick Sort (Rekurencyjny) ------------------------ #
def divide_tab(data, low, high, pivot_type):
    if pivot_type == "random":
        rand_idx = random.randint(low, high)
        data[low], data[rand_idx] = data[rand_idx], data[low]
    
    pivot = data[low]
    i = low + 1
    
    for j in range(low + 1, high + 1):
        if data[j] < pivot:
            data[i], data[j] = data[j], data[i]
            i += 1
    
    data[low], data[i - 1] = data[i - 1], data[low]
    return i - 1

def quicksort_check(data, low, high, pivot_type):
    if low < high:
        pivot_idx = divide_tab(data, low, high, pivot_type)
        quicksort_check(data, low, pivot_idx - 1, pivot_type)
        quicksort_check(data, pivot_idx + 1, high, pivot_type)

def quick_sort(arr, pivot_type = "left"):
    data = arr[:]
    quicksort_check(data, 0, len(data) - 1, pivot_type)
    return data
