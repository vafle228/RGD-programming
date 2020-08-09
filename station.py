import time


class Station:
    def __init__(self, ways):
        self.ways = ways
        self.arrived_trains = []
        self.is_test = False

    def fill(self, train):
        s_ways = None
        if (time.strptime(time.strftime('%H%M'), '%H%M') == train.arrive_time) and (train not in self.arrived_trains) \
                or self.is_test:
            for way in self.ways:
                if train.capacity <= way.capacity and way.filling is None \
                        and (s_ways is None or s_ways.capacity > way.capacity):
                    s_ways = way

            if s_ways is not None:
                s_ways.filling = train
                self.arrived_trains.append(train)
                print('Поезд {train_name} занял линию {name}'.format(name=s_ways.name, train_name=s_ways.filling.name))
                return train
            elif sorted(self.ways, key=lambda way: way.capacity, reverse=True)[0].capacity < train.capacity:
                print('Поезд {} не заехал на станцию'.format(train.name))

                return train
        return None

    def out_fill(self, train):
        if (time.strptime(time.strftime('%H%M'), '%H%M') == train.out_time) and (train in self.arrived_trains) \
                or self.is_test:
            for way in self.ways:
                if way.filling is None:
                    continue
                elif way.filling.name == train.name:
                    print('Поезд {train_name} покинул линию {name}'.format(name=way.name, train_name=way.filling.name))
                    way.filling = None
                    return train
        return None
