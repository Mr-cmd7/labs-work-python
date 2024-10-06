from Movement import *

if __name__ == '__main__':
    speedInput = float(input('Введите скорость (м/сек): '))
    timeInput = int(input('Введите время (сек): '))

    movement = Movement(speedInput, timeInput)

    print(movement)

    distance = movement.calculate_distance()
    print(f"Пройденное расстояние: {distance} метров")