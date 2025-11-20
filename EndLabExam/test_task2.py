from task2 import binary_search

def _check_bounds(arr, idx, comps):
    if len(arr) == 0:
        # empty array: no comparisons, not found
        assert idx == -1
        assert comps == 0
    else:
        # if found, index must be valid and point to the target
        if idx != -1:
            assert 0 <= idx < len(arr)
        # comparisons should be at least 1 and at most len(arr) (safe upper bound)
        assert comps >= 1
        assert comps <= len(arr)

def test_empty_array():
    idx, comps = binary_search([], 42)
    assert idx == -1 and comps == 0
    print("✓ test_empty_array passed")

def test_single_element_found():
    arr = [5]
    idx, comps = binary_search(arr, 5)
    assert idx == 0
    assert comps == 1
    print("✓ test_single_element_found passed")

def test_single_element_not_found():
    arr = [5]
    idx, comps = binary_search(arr, 3)
    assert idx == -1
    assert comps == 1
    print("✓ test_single_element_not_found passed")

def test_various_positions():
    test_cases = [
        ([1,2,3,4,5], 1, 0),
        ([1,2,3,4,5], 3, 2),
        ([1,2,3,4,5], 5, 4),
        ([1,2,3,4,5], 6, -1),
        ([-10, -5, 0, 5, 10], -5, 1),
    ]
    for arr, target, expected in test_cases:
        idx, comps = binary_search(arr, target)
        if expected == -1:
            assert idx == -1
        else:
            assert idx == expected
        _check_bounds(arr, idx, comps)
    print("✓ test_various_positions passed")

def test_duplicates():
    arr = [1, 2, 2, 2, 3]
    idx, comps = binary_search(arr, 2)
    assert idx in {1,2,3}
    _check_bounds(arr, idx, comps)
    print("✓ test_duplicates passed")

def test_target_out_of_range():
    arr = [0, 10, 20, 30, 40]
    idx_low, comps_low = binary_search(arr, -100)
    idx_high, comps_high = binary_search(arr, 100)
    assert idx_low == -1
    assert idx_high == -1
    _check_bounds(arr, idx_low, comps_low)
    _check_bounds(arr, idx_high, comps_high)
    print("✓ test_target_out_of_range passed")

def test_even_length_array():
    arr = [2,4,6,8]
    idx, comps = binary_search(arr, 6)
    assert idx == 2
    _check_bounds(arr, idx, comps)
    print("✓ test_even_length_array passed")

if __name__ == "__main__":
    test_empty_array()
    test_single_element_found()
    test_single_element_not_found()
    test_various_positions()
    test_duplicates()
    test_target_out_of_range()
    test_even_length_array()
    print("\nAll tests passed!")