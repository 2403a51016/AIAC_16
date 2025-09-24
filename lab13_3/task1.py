import math
def rectangle_area(x, y):
    return x * y
def square_area(x):
    return x * x
def circle_area(x):
    return math.pi * x * x
def calculate_area(shape, x, y=0):
    area_functions = {
        "rectangle": lambda: rectangle_area(x, y),
        "square": lambda: square_area(x),
        "circle": lambda: circle_area(x)
    }
    try:
        return area_functions[shape]()
    except KeyError:
        raise ValueError(f"Unsupported shape: {shape}")
#example usage:
if __name__ == "__main__":
    print(calculate_area("rectangle", 5, 10))  # Output: 50
    print(calculate_area("square", 4))          # Output: 16
    print(calculate_area("circle", 3))          # Output: 28.274333882308138
    try:
        print(calculate_area("triangle", 5, 10)) # Raises ValueError
    except ValueError as e:
        print(e)  # Output: Unsupported shape: triangle