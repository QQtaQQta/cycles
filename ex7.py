num = int(input("введите целое положительное число: "))
sum_of_even_digits = 0

while num > 0:
    digit = num % 10
    if digit % 2 == 0:
        sum_of_even_digits += digit
    num //= 10
    
print("сумма четных цифр числа: ", sum_of_even_digits)