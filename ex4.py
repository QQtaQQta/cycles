n = int(input("введите число: "))
factorial = 1

for i in range(1, n+1):
    factorial *= i

print(f"Факториал числа {n} равен {factorial}")