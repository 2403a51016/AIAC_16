#calculator function
def calculator(a,b,operation):
    if operation=="add":
        return a+b
    elif operation=="subtract":
        return a-b
    elif operation=="multiply":
        return a*b
    elif operation=="divide":
        if b!=0:
            return a/b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
    
# Example usage
result1 = calculator(10, 5, "add")
print("Addition:", result1)
        
    