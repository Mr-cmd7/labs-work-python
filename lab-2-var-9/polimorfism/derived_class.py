from base_class import Athlete

class FirstPlaceAthlete(Athlete):
    def __init__(self, last_name, num_competitions, sum_places, first_place):
        super().__init__(last_name, num_competitions, sum_places)
        self.first_place = first_place

    def quality(self):
        if self.first_place:
            return 1.5 * super().quality()
        else:
            return super().quality()

    def __repr__(self):
        return f'{super().__repr__()}Занял Первое Место: {"Да" if self.first_place else "Нет"}\n' \
               f'Качество: {self.quality()}\n'