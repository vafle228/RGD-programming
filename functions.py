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


def main(trains, station):

    for train in trains:
        if (train.capacity is None) or (train.name is None) \
                or (train.arrive_time is None) or (train.out_time is None):
            trains.remove(train)

    trains = sorted(trains, key=lambda train: (train.out_time.tm_hour * 60 + train.arrive_time.tm_min), reverse=True)

    while trains or station.arrived_trains:
        trains_cleaner(trains_input(trains, station.fill), trains)

        trains_cleaner(trains_input(station.arrived_trains, station.out_fill), station.arrived_trains)


def valid(data, p_type):
    data = str(data)
    if p_type == 'int':
        if data.isdigit() and int(data) >= 0:
            return int(data)
        print('Некорректные числовые данные')
        return None
    if p_type == 'time':
        try:
            if ':' in data:
                data = data.split(':')[0] + data.split(':')[1]
            return time.strptime(data, '%H%M')
        except ValueError:
            print('Некорректные временные данные')
            return None
    if p_type == 'train_name':
        if (len(data) == 4 and data[3].isalpha()) or (len(data) == 5 and data[4].isalpha()):
            return data
        print('Некорректная форма данных id поезда')
        return None
