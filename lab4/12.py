n = int(input("Enter the number: "))
product = 1

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    for i in range(1, n + 1):
        product *= i
    print(f"The factorial of {n} is {product}")