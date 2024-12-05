from base_class import Athlete
from derived_class import FirstPlaceAthlete

if __name__ == "__main__":
    # Спортсмены без места
    athlete1 = Athlete('Иванов', 10, 20)
    athlete2 = Athlete('Петров', 8, 15)

    # Выводим информацию о спортсменах
    print("Информация о спортсменах:")
    print(athlete1)
    print(athlete2)

    # Спортсмен с 1 местом
    athlete3 = FirstPlaceAthlete('Сидоров', 12, 18, True)

    # Выводим информацию о спортсмене, занявшем первое место
    print("\nИнформация о спортсмене, занявшем первое место:")
    print(athlete3)