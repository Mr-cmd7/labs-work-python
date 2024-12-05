class Movement:
    def __init__(self, speed, time):
        self.speed = speed
        self.time = time

    def __str__(self):
        return f"Скорость: {self.speed} м/сек, Время: {self.time} сек"

    def calculate_distance(self):
        distance = self.speed * self.time
        return distance

