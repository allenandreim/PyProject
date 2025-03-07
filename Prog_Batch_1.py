a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Bigger number:", max(a, b))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Equal" if a == b else "Not Equal")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Sum:", a + b)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Product:", a * b)

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if b != 0:
    print("Quotient:", a / b)
else:
    print("Division by zero is not allowed.")

a = float(input("Enter base number: "))
b = float(input("Enter exponent: "))
print("Result:", a ** b)

total = 0
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    total += num
print("Total sum:", total)

odd_count = 0
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 != 0:
        odd_count += 1
print("Odd numbers count:", odd_count)

for i in range(0, 101, 2):
    print(i, end=" ")

for i in range(101):
    if i % 10 != 0:
        print(i, end=" ")

