#3
n = input("Введите положительное число: ")
print(f"{n} + {n + n} + {n + n + n} = {int(n) + int(n + n) + int(n + n + n)}")

#4
num_init = int(input('Введите целое положительное число: '))
maximum = num_init % 10
num = num_init

while num > 0:
    digit = num % 10
    if digit > maximum:
        maximum = digit

    if digit == 9:
        break

    num //= 10 # num = num // 10
    print(num)

print("Наибольшая цифра в числе {num_init} равна {maximum}")