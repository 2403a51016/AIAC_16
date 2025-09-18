def parse_time_to_minutes(time_str):
    """Convert HH:MM string to minutes since midnight."""
    hours, minutes = map(int, time_str.split(":"))
    return hours * 60 + minutes

def is_surge_time(time_str):
    """
    Returns True if time is strictly after 18:00 (i.e., 18:01 or later).
    """
    minutes = parse_time_to_minutes(time_str)
    return minutes > 18 * 60  # 18:00 is 1080 minutes

def calculate_fares(rides, base_per_km, surge_multiplier):
    """
    Calculates fare for each ride:
    - fare = km * base_per_km * surgeMultiplier (if after 18:00)
    - else fare = km * base_per_km
    - Each fare rounded to 2 decimals.
    - Does not mutate input.
    """
    fares = []
    for ride in rides:
        km = ride['km']
        time = ride['time']
        if is_surge_time(time):
            fare = km * base_per_km * surge_multiplier
        else:
            fare = km * base_per_km
        fares.append(round(fare, 2))
    return fares

def main():
    print("Agritech Fare Calculator")
    try:
        n = int(input("Number of rides: "))
        rides = []
        for i in range(n):
            print(f"Ride {i+1}:")
            time = input("  Time (HH:MM): ").strip()
            km = float(input("  Distance (km): "))
            rides.append({'time': time, 'km': km})
        base_per_km = float(input("Base per km rate: "))
        surge_multiplier = float(input("Surge multiplier (e.g., 2 for 2x): "))
    except Exception as e:
        print(f"Input error: {e}")
        return

    fares = calculate_fares(rides, base_per_km, surge_multiplier)
    print("Fares:", fares)

def test_fare_calculator():
    # Test edge cases: before, at, and after 18:00
    rides = [
        {'time': '08:00', 'km': 3.0},   # no surge
        {'time': '18:00', 'km': 5.0},   # exactly 18:00, no surge
        {'time': '18:01', 'km': 5.0},   # after 18:00, surge
        {'time': '18:30', 'km': 2.5},   # after 18:00, surge
    ]
    base = 22.0
    surge = 2.0
    expected = [
        66.0,      # 3.0 * 22.0 = 66.0
        110.0,     # 5.0 * 22.0 = 110.0
        220.0,     # 5.0 * 22.0 * 2 = 220.0
        110.0      # 2.5 * 22.0 * 2 = 110.0
    ]
    result = calculate_fares(rides, base, surge)
    assert result == expected, f"Expected {expected}, got {result}"
    print("Test passed.")

if __name__ == "__main__":
    # Edge case: exactly 18:00 is NOT surge, after 18:00 (e.g., 18:01) is surge.
    test_fare_calculator()
    main()
'''
"implement a fare calculator for an e-commerce app. 
fare is km * base_per_km * surgeMultiplier, where surge applies only after 18:00 (not at 18:00). 
input is a list of rides with time (HH:MM) and km.
round each fare to 2 decimals, avoid mutating input, and allow user input.
include a testcase."'''