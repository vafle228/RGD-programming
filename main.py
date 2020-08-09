from station import Station
from station_elements import Way, Train
from functions import main

ways = [Way(11, 'линия 10'), Way(10, 'Линия 12')]
trains = [Train(10, '129q', '1015', '1016')]
station = Station(ways)

main(trains, station)
