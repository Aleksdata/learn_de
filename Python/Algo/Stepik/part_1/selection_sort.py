def selection_sort(values):
    """
    Сортировка выбором.
    """
    # Перебираем все элементы.
    for i in range(len(values) - 1):
        min_idx = i
        # Перебираем оставшиеся элементы.
        for j in range(i + 1, len(values)):
            # Ищем минимальное значение.
            if values[min_idx] > values[j]:
                min_idx = j

        if i != min_idx:
            # Меняем минимальное значение с текущим элементом основного цикла.
            values[i], values[min_idx] = values[min_idx], values[i]


initial: list = [2, 8, 7, 5, 3, 6]
selection_sort(initial)
print(initial)