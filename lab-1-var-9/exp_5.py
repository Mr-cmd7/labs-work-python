# Получить упорядоченный список слов и количество их встречаемости.

def word_count(_lines):
    word_dict = {}

    for line in _lines:
        words = line.split()
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

    sorted_words = sorted(word_dict.items())

    for word, count in sorted_words:
        print(f"{word}: {count}")


num_lines = 3
lines = [
    "hello world",
    "hello from the other side",
    "world of Python"
]
word_count(lines)
