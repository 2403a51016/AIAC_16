import random
import time
from typing import List, Tuple

"""
task2.py

Simple implementations of Linear Search and Binary Search with comparison counting
and a small timing comparison. Meant to be run as a script.
"""


def linear_search(arr: List[int], target: int) -> Tuple[int, int]:
    """Return (index, comparisons). Index is -1 if not found."""
    comps = 0
    for i, v in enumerate(arr):
        comps += 1
        if v == target:
            return i, comps
    return -1, comps

def binary_search(arr: List[int], target: int) -> Tuple[int, int]:
    """Iterative binary search on sorted arr. Return (index, comparisons)."""
    lo, hi = 0, len(arr) - 1
    comps = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        comps += 1
        if arr[mid] == target:
            return mid, comps
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, comps

# -----------------------
# Small correctness tests
# -----------------------
def _sanity_checks():
    a = [5, 1, 9, 3, 7]
    # linear search
    assert linear_search(a, 9)[0] == 2
    assert linear_search(a, 2)[0] == -1
    # binary search must be used on sorted array
    s = sorted(a)
    assert binary_search(s, 9)[0] == s.index(9)
    assert binary_search(s, 2)[0] == -1

# -----------------------
# Timing comparisons
# -----------------------
def time_search(search_fn, arr, target, trials=10):
    """Time the search function (arr must be prepared as needed)"""
    start = time.perf_counter()
    for _ in range(trials):
        search_fn(arr, target)
    end = time.perf_counter()
    return (end - start) / trials

def demo():
    
    random.seed(0)
    sizes = [1000, 5000, 20000]
    trials = 50

    print("Size | linear(s) avg | linear comps avg | binary(s) avg (sorted) | binary comps avg")
    for n in sizes:
        arr = [random.randint(0, n * 10) for _ in range(n)]
        # pick targets: present and absent mix
        present = random.choice(arr)
        absent = -1  # assume negative not in generated positives
        # prepare sorted copy for binary search
        sorted_arr = sorted(arr)

        # time linear search for present and absent, average them
        t_lin_present = time_search(linear_search, arr, present, trials)
        t_lin_absent = time_search(linear_search, arr, absent, trials)
        t_lin = (t_lin_present + t_lin_absent) / 2

        # get average comparisons by running multiple times
        comps_lin = 0
        for _ in range(trials):
            _, c = linear_search(arr, random.choice([present, absent]))
            comps_lin += c
        comps_lin /= trials

        # binary search times (on sorted array)
        t_bin_present = time_search(binary_search, sorted_arr, present, trials)
        t_bin_absent = time_search(binary_search, sorted_arr, absent, trials)
        t_bin = (t_bin_present + t_bin_absent) / 2

        comps_bin = 0
        for _ in range(trials):
            _, c = binary_search(sorted_arr, random.choice([present, absent]))
            comps_bin += c
        comps_bin /= trials

        print(f"{n:5d} | {t_lin:.6f} | {comps_lin:.2f} | {t_bin:.6f} | {comps_bin:.2f}")

    # show cost of sorting vs binary search when array unsorted
    n = 20000
    arr = [random.randint(0, n * 10) for _ in range(n)]
    sorted_time = time.perf_counter()
    sorted(arr)
    sorted_time = time.perf_counter() - sorted_time
    print(f"\nSorting a {n} element array (one shot): {sorted_time:.6f} seconds")
    print("Note: Binary search requires a sorted array; include sort cost if the array isn't already sorted.")

if __name__ == "__main__":
    _sanity_checks()
    demo()