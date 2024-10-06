#16

def find_min_year(file_name):
    min_year = float('inf')

    with open(file_name, 'r') as file:
        for line in file:
            date_parts = line.strip().split('.')
            if len(date_parts) == 3:
                day, month, year = date_parts
                try:
                    year = int(year)
                    if year < min_year:
                        min_year = year
                except ValueError:
                    print(f"Неверный формат года в строке: {line.strip()}")

    return min_year if min_year != float('inf') else None

file_name = "assets/dates.txt"
min_year = find_min_year(file_name)
if min_year is not None:
    print(f"Год с наименьшим номером: {min_year}")
else:
    print("Не удалось найти год.")
