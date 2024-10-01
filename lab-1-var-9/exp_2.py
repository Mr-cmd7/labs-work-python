# Удалить из двумерного массива все строки с четными номерами.

def remove_even_rows(array):
    array = list(array)
    new_array = [row for i, row in enumerate(array) if i % 2 != 0]

    while len(new_array) < len(array):
        new_array.append([0] * len(array[0]))

    return tuple(new_array)


massive = ((1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12))
result = remove_even_rows(massive)
print(result)
