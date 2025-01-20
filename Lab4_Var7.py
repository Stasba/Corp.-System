n= int(input("натуральное n - "))

current_factorial = 1
factorial_sum = 0

for i in range(1, n + 1):
    current_factorial *=i
    factorial_sum +=current_factorial
print("Сумма от 1 до", n, "равна", factorial_sum)
