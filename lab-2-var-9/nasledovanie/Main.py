from mypackage.Object import Object
from mypackage.MovingObject import MovingObject

# Создаем объект базового класса
obj = Object(mass=10, velocity=20)
print(f'Объект: {obj}')
print(f'Кинетическая энергия: {obj.get_kinetic_energy()} Дж')

# Создаем объект производного класса
moving_obj = MovingObject(mass=15, velocity=30, force=50)
print(f'Движущийся объект: {moving_obj}')
print(f'Работа силы при перемещении на 100 м: {moving_obj.calculate_work(distance=100)} Дж')