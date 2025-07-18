def factorial_iterative(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

test_numbers = [0, 5, 10, 25, 50, 100]

print("Iterative Factorials:")
for num in test_numbers:
    print(f"{num}! = {factorial_iterative(num)}")

print("\nRecursive Factorials:")
for num in test_numbers:
    print(f"{num}! = {factorial_recursive(num)}")