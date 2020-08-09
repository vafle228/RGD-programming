import time


def trains_cleaner(rubbish, array):
    for train in rubbish:
        array.remove(train)


def trains_input(trains, function):
    result = []
    flag = None
    for train in trains:
        flag = function(train)
        if flag:
            result.append(flag)
    return result


def valid(data, p_type):
    data = str(data)
    if p_type == 'int':
        return int_check(data)
    if p_type == 'time':
        return time_check(data)
    if p_type == 'train_name':
        return train_name_check(data)
    if p_type == 'way_name':
        return way_name_check(data)


def time_check(data):
    if ':' in data:
        data = data.split(':')[0] + data.split(':')[1]
    try:
        return time.strptime(data, '%H%M')
    except ValueError:
        raise ValueError('Некорректные временные данные')


def train_name_check(data):
    if (data[-1].isalpha() and data[0:-1].isdigit()) and (len(data) == 4 or len(data) == 5):
        return data
    raise ValueError('Некорректный id')


def int_check(data):
    if data.isdigit() and 0 < int(data) < 100:
        return int(data)
    raise ValueError('Некорректные числовые данные')


def way_name_check(data):
    if data.isdigit() and 0 < int(data) < 100:
        return int(data)
    raise ValueError('Некорректоное id пути')


def main(trains, station):
    for train in trains:
        if (train.capacity is None) or (train.name is None) \
                or (train.arrive_time is None) or (train.out_time is None):
            trains.remove(train)

    trains = sorted(trains, key=lambda train: (train.out_time.tm_hour * 60 + train.arrive_time.tm_min), reverse=True)

    while trains or station.arrived_trains:
        trains_cleaner(trains_input(trains, station.fill), trains)

        trains_cleaner(trains_input(station.arrived_trains, station.out_fill), station.arrived_trains)
