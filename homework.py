base = int(input("Please enter the base number: "))
n = int(input("Please enter the power: "))

result = 1
i = 1

while i <= n:
    result = result * base
    i = i + 1

print("The answer is", result)
