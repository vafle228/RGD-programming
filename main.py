import time


class Station:
    def __init__(self, ways):
        self.ways = ways

    def fill(self, train):
        s_ways = None
        for way in self.ways:
            if (time.strptime(time.strftime('%H%M'), '%H%M') == train.arrive_time) and \
               (train not in arrived_trains):
                if train.capacity <= way.capacity and way.filling is None \
                        and (s_ways is None or s_ways.capacity > way.capacity):
                    s_ways = way

            if s_ways is not None:
                s_ways.filling = train
                print('Поезд {train_name} занял линию {name}'.format(name=s_ways.name,
                                                                     train_name=s_ways.filling.name)
                return train
            
            if (time.strptime(time.strftime('%H%M'), '%H%M') == train.arrive_time) and \
               (train not in arrived_trains):
                print('Поезд {} не заехал на станцию'.format(train.name))
                trains.remove(train)
        return None

    def trains_input(self, trains, function):
        result = []
        flag = None
        for train in trains:
            flag = function(train)
            if flag:
                result.append(flag)
        return result

    def out_fill(self, train):
        for way in self.ways:
            if way.filling is None:
                continue
            elif way.filling.name == train.name:
                print('Поезд {train_name} покинул линию {name}'.format(name=way.name,
                                                                       train_name=way.filling.name))
                way.filling = None
                return train
        return None


class Way:
    def __init__(self, capacity, name, train=None):
        self.capacity = valid(capacity, 'int') or 1
        self.name = name
        self.filling = train


class Train:
    def __init__(self, capacity, name, arrive_time, out_time):
        self.capacity = valid(capacity, 'int') or 1
        self.name = name
        self.arrive_time = valid(arrive_time, 'time') or time.strptime('0000', '%H%M')
        self.out_time = valid(out_time, 'time') or time.strptime('0000', '%H%M')


def valid(data, p_type):
    data = str(data)
    if p_type == 'int':
        if data.isdigit() and int(data) >= 0:
            return int(data)
        return None
    if p_type == 'time':
        try:
            if ':' in data:
                data = data.split(':')[0] + data.split(':')[1]
            return time.strptime(data, '%H%M')
        except ValueError:
            return None
    return None


ways = [Way(10, 'a')]
trains = [Train(10, 'qwerty1', '1450', '1530')]
station = Station(ways)

arrived_trains = []
outing_trains = []

while trains:

    arrived_trains = station.trains_input(trains, station.fill)

    for arrived_train in arrived_trains:
        if arrived_train in trains:
            trains.remove(arrived_train)

    outing_trains = station.trains_input(arrived_trains, station.out_fill)

    for outing_train in outing_trains:
        arrived_trains.remove(outing_train)
        outing_trains.remove(outing_train)
