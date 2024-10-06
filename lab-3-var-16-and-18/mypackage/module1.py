def find_min_year(filename):
    with open(filename, 'r') as file:
        years = []
        for line in file:
            day, month, year = map(int, line.strip().split('.'))
            years.append(year)

    return min(years)


if __name__ == "__main__":
    min_year = find_min_year('resources/dates.txt')
    print(f"Год с наименьшим номером: {min_year}")
