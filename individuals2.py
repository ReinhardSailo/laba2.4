def find_max_absolute_index(arr):
    max_index = 0
    max_value = abs(arr[0])

    for i in range(1, len(arr)):
        if abs(arr[i]) > max_value:
            max_index = i
            max_value = abs(arr[i])

    return max_index

def find_sum_after_positive(arr):
    sum_after_positive = 0
    positive_found = False

    for num in arr:
        if positive_found:
            sum_after_positive += num
        elif num > 0:
            positive_found = True

    return sum_after_positive

# Ввод списка вещественных чисел
elements = [float(input(f"Введите элемент {i+1}: ")) for i in range(10)]

# Находим номер максимального по модулю элемента и сумму элементов после первого положительного
max_absolute_index = find_max_absolute_index(elements)
sum_after_positive = find_sum_after_positive(elements)

# Вывод результатов
print(f"Номер максимального по модулю элемента: {max_absolute_index + 1}")
print(f"Сумма элементов после первого положительного: {sum_after_positive}")
