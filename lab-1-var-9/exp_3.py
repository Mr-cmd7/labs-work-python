# Переставить соседние элементы списка.

def swap_elements(lists):
    for i in range(0, len(lists) - 1, 2):
        lists[i], lists[i + 1] = lists[i + 1], lists[i]
    return lists


lst = [1, 2, 3, 4, 5]
result = swap_elements(lst)
print(result)
