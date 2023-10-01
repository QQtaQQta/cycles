num = int(input("введите целое положительное число: "))

while num > 0:
    digit = num % 10
    print(digit, end=" ")
    num //= 10
    
"""тут цифры будут выводиться в обратном порядке, но можно сделать список и вывести их адекватно
num = int(input("введите целое положительное число: "))

digits = []
while num > 0:
    digit = num % 10
    digits.append(digit)
    num //= 10

digits.reverse()
for digit in digits:
    print(digit, end=" ")"""