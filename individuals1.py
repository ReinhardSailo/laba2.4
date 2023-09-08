def find_negative_multiples_of_seven_sum(arr):
    sum_negatives = 0
    count = 0

    for num in arr:
        if num < 0 and num % 7 == 0:
            sum_negatives += num
            count += 1

    return sum_negatives, count

# Ввод списка из 10 элементов
A = []
for i in range(10):
    num = int(input(f"Введите {i+1}-й элемент: "))
    A.append(num)

# Находим сумму отрицательных элементов кратных 7 и их количество
sum_result, count_result = find_negative_multiples_of_seven_sum(A)

# Вывод результатов
print(f"Сумма отрицательных элементов кратных 7: {sum_result}")
print(f"Количество таких элементов: {count_result}")
