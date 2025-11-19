import random
def choose_pivot_index(arr, low, high, strategy='median3'):
    if strategy == 'first':
        return low
    if strategy == 'last':
        return high
    if strategy == 'middle':
        return (low + high) // 2
    if strategy == 'random':
        return random.randint(low, high)
    # median-of-three: choose median of low, mid, high
    mid = (low + high) // 2
    trio = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    trio.sort(key=lambda x: x[0])
    return trio[1][1]
def partition(arr, low, high, strategy):
    pivot_index = choose_pivot_index(arr, low, high, strategy)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # move pivot to end (Lomuto)
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i 
def quick_sort(arr, low=0, high=None, strategy='median3'):
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high, strategy)
        quick_sort(arr, low, p - 1, strategy)
        quick_sort(arr, p + 1, high, strategy)
if __name__ == '__main__':
    data = [90, 12, 77, 23, 5, 41, 68]
    print("Original:", data)
    # Choose pivot strategy: 'first', 'last', 'middle', 'random', 'median3'
    quick_sort(data, strategy='median3')
    print("Sorted:", data)