base = int(input("введите число: "))
exponent = int(input("введите степень (должна быть положительной): "))

if (exponent < 0)
    print("степень не положительная")
else
    result = 1
    for i in range(exponent):
        result *= base

    print(f"{base} в степени {exponent} равно {result}")