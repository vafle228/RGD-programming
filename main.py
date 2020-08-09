from station import Station
from station_elements import Way, Train


def trains_input(trains, function):
    result = []
    flag = None
    for train in trains:
        flag = function(train)
        if flag:
            result.append(flag)
    return result


def trains_cleaner(rubbish, array):
    for train in rubbish:
        array.remove(train)


ways = [Way(11, 'линия 10'), Way(10, 'Линия 12')]
trains = [Train(10, '129q', '2300', '2354')]
station = Station(ways)


for train in trains:
    if (train.capacity is None) or (train.name is None) \
            or (train.arrive_time is None) or (train.out_time is None):
        trains.remove(train)

trains = sorted(trains, key=lambda train: (train.out_time.tm_hour * 60 + train.arrive_time.tm_min), reverse=True)

while trains:

    trains_cleaner(trains_input(trains, station.fill), trains)

    trains_cleaner(trains_input(station.arrived_trains, station.out_fill), station.arrived_trains)

