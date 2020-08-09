from station import Station
from station_elements import Way, Train
from functions import main

try:
    ways = [Way(12, '12'), Way(10, '12')]
    trains = [Train(10, '123q', '2000', '1016')]
    station = Station(ways)
except TypeError:
    raise TypeError('Отсутсвуют позиционные аргументы')

main(trains, station)
