def rolling_mean(xs, w):
    """
    Computes rolling mean (moving average) with window size w.
    Guards against invalid window sizes.
    """
    if w <= 0 or w > len(xs):
        raise ValueError("Invalid window size: must be > 0 and <= length of input list.")
    means = []
    # Fix: iterate up to len(xs) - w + 1 to include all valid windows
    for i in range(len(xs) - w + 1):
        window = xs[i:i+w]
        means.append(sum(window) / w)
    return means

def test_rolling_mean():
    print("Running test cases...")

    # Failing test first (would fail if off-by-one bug present)
    assert rolling_mean([13, 14, 15, 16], 2) == [13.5, 14.5, 15.5], "Failed on [13,14,15,16], w=2"

    # Provided sample
    assert rolling_mean([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]
    assert rolling_mean([10, 20, 30], 1) == [10.0, 20.0, 30.0]
    assert rolling_mean([2, 4, 6, 8], 4) == [5.0]

    # Edge cases: invalid window sizes
    try:
        rolling_mean([1, 2], 0)
        assert False, "Expected ValueError for w = 0"
    except ValueError:
        pass

    try:
        rolling_mean([1, 2], 3)
        assert False, "Expected ValueError for w > len(xs)"
    except ValueError:
        pass

    print(" All tests passed.\n")

def main():
    print("Rolling Mean Calculator (Agritech KPI)")
    print("Enter your data to compute moving averages (rolling means).")

    try:
        xs_input = input("Enter a list of numbers separated by spaces: ")
        xs = list(map(float, xs_input.strip().split()))
        w = int(input("Enter window size (positive integer): "))
        result = rolling_mean(xs, w)
        print("\nRolling averages:", result)
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")

if __name__ == "__main__":
    test_rolling_mean()
    main()
    '''
"fix an off-by-one bug in a rolling mean function for an e-commerce KPI calculation.
 guard against invalid window sizes (w <= 0 or w > len(xs)),
  preserve a simple O(n * w) solution, 
add a failing test first, then fix the logic,
 verify with sample input 
and finally allow user input for the list and window size."'''