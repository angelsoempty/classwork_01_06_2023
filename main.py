a = int(input('Введіть перше число: '))
b = int(input('Введіть друге число: '))

sum = 0
for i in range(a, b + 1):
    sum += i
print(f'Сума чисел діапазону {sum}')