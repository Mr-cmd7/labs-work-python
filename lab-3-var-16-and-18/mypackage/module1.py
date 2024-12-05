def find_min_year(filename):
    with open(filename, 'r') as file:
        years = []
        for line in file:
            day, month, year = map(int, line.strip().split('.'))
            years.append(year)

    return min(years)
