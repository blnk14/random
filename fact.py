# Calculate the factorial value
def calculate_factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if n == 0:
        return 1

    result = 1
    for number in range(1, n + 1):
        result = result * number
        
    return result

# 100! value
fact = calculate_factorial(100)

# Convert to string to iterate through
values = str(fact)

total_sum = 0
for value in values:
    total_sum += int(value)

print(f"\nThe sum of the digits in 100! is: {total_sum}")