# Найти индекс элемента массива, равного 13

def find_index(arr, target=13):
    try:
        index = arr.index(target)
        print(f"Индекс элемента {target}: {index}")
    except ValueError:
        print(f"Число {target} в массиве не найдено.")


array = (1, 2, 3, 13, 5)
find_index(array)

