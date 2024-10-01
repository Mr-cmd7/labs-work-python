# Определить количество забастовок в стране.

def count_strikes(N, K, schedules):
    if len(schedules) != K:
        raise ValueError("Количество графиков забастовок не соответствует K.")

    strikes = set()

    for a, b in schedules:
        day = a
        while day <= N:
            if day % 7 != 6 and day % 7 != 0:  # Суббота - 6, Воскресенье - 0
                strikes.add(day)
            day += b

    return len(strikes)


N = 30  # Количество дней в месяце
K = 3  # Количество партий
schedules = [(1, 3), (2, 5), (10, 10)]

result = count_strikes(N, K, schedules)
print("Количество забастовок:", result)
