class Athlete:
    def __init__(self, last_name, num_competitions, sum_places):
        self.last_name = last_name
        self.num_competitions = num_competitions
        self.sum_places = sum_places

    def quality(self):
        if self.sum_places == 0:
            return None
        else:
            return self.num_competitions / self.sum_places

    def __repr__(self):
        return f'Фамилия: {self.last_name}\n' \
               f'Количество соревнований: {self.num_competitions}\n' \
               f'Сумма мест: {self.sum_places}\n' \
               f'Качество: {self.quality()}\n'