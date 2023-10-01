num = int(input("введите целое положительное число: "))
sum_of_digits = 0
product_of_digits = 1

while num > 0:
    digit = num % 10
    sum_of_digits += digit
    product_of_digits *= digit
    num //= 10

print("сумма цифр числа: ", sum_of_digits)
print("проивзедение цифр числа: ", product_of_digits)