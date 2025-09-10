def student_discount(price):
    return price * 0.9 if price > 1000 else price * 0.95

def regular_discount(price):
    return price * 0.85 if price > 2000 else price

def discount(price, category):
    return student_discount(price) if category == "student" else regular_discount(price)
print(discount(1200, "student"))   # Output: 1080.0
print(discount(800, "student"))    # Output: 760.0
print(discount(2500, "regular"))   # Output: 2125.0
print(discount(1800, "regular"))   # Output: 1800