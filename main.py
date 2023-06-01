sum = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print(f'Сума парних чисел в діапазоні 1 до 100 {sum}')