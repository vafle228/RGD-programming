from station import Station
from station_elements import Way, Train


ways = [Way(12, 'линия 10'), Way(13, 'Линия 12')]
trains = [Train(10, 'поезд 1', '1131', '1017'), Train(10, 'поезд 2', '1016', '1004'),
          Train(10, 'поезд 3', '1016', '1005')]
station = Station(ways)

outing_trains = []

for train in trains:
    if (train.capacity is None) or (train.name is None) \
            or (train.arrive_time is None) or (train.out_time is None):
        trains.remove(train)

trains = sorted(trains, key=lambda train: (train.out_time.tm_hour * 60 + train.arrive_time.tm_min), reverse=True)

while trains:

    station.fill(trains)

    for arrived_train in station.arrived_trains:
        if arrived_train in trains:
            trains.remove(station.arrived_train)

    station.out_fill(trains)
