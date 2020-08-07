import time


class Station:
    def __init__(self, ways):
        self.ways = []
        for i in range(ways):
            capacity = int(valid_input('Введите длину линии: ', 'int'))
            name = input('Введите название линии: ')
            self.ways.append(Way(capacity, name))

    def fill(self, train):
        s_ways = None
        for way in self.ways:
            if train.capacity <= way.capacity and way.filling is None \
               and (s_ways is None or s_ways.capacity > way.capacity):
                s_ways = way

            if s_ways is not None:
                s_ways.filling = train
                return 'Поезд {train_name} занял линию {name}'.format(name=s_ways.name,
                                                                      train_name=s_ways.filling.name)
        return None

    def out_fill(self, train):
        for way in self.ways:
            if way.filling is None:
                continue
            elif way.filling.name == train.name:
                out = 'Поезд {train_name} покинул линию {name}'.format(name=way.name,
                                                                       train_name=way.filling.name)
                way.filling = None
                return out
        return None


class Way:
    def __init__(self, capacity, name, train=None):
        self.capacity = int(capacity)
        self.name = name
        self.filling = train


class Train:
    def __init__(self, name, capacity, arrive_time, out_time):
        self.capacity = int(capacity)
        self.name = name
        self.arrive_time = arrive_time
        self.out_time = out_time


def valid_input(message, p_type):
    while True:
        data = input(message)
        if p_type == 'int':
            if data.isdigit() and int(data) >= 0:
                return data
            continue
        if p_type == 'time':
            try:
                if ':' in data:
                    data = data.split(':')[0] + data.split(':')[1]
                return time.strptime(data, '%H%M')
            except ValueError:
                continue


trains = []
arrived_trains = []

station = Station(int(valid_input('Введите сколько линий: ', 'int')))

n = int(valid_input('Ввдети сколько поездов подъезжает: ', 'int'))

for _ in range(n):
    train_name = input('Введите id поезда: ')
    train_capacity = valid_input('Введите длинну поезда: ', 'int')
    train_arriving = valid_input('Введите время прибытия: ', 'time')
    train_outing = valid_input('Введите время отбытия: ', 'time')

    trains.append(Train(train_name, train_capacity, train_arriving, train_outing))

trains = sorted(trains, key=lambda train: (train.out_time.tm_hour * 60 + train.out_time.tm_min) -
                                          (train.arrive_time.tm_hour * 60 + train.arrive_time.tm_min))

while True:
    for train in trains:
        if (time.strptime(time.strftime('%H%M'), '%H%M') == train.arrive_time) and \
           (train not in arrived_trains):
            result = station.fill(train)
            if not result:
                print('Поезд {} не смог заехать'.format(train.name))
                trains.remove(train)
                continue
            print(result)
            arrived_trains.append(train)

    for train in arrived_trains:
        if train in trains:
            trains.remove(train)

    for arrived_train in arrived_trains:
        if time.strptime(time.strftime('%H%M'), '%H%M') == arrived_train.out_time:
            print(station.out_fill(arrived_train))
            arrived_trains.remove(arrived_train)
