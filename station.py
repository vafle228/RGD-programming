import time


class Station:
    def __init__(self, ways):
        self.ways = ways
        self.arrived_trains = []

        for way in self.ways:
            if way.capacity is None:
                self.ways.remove(way)

    def fill(self, trains):
        s_ways = None
        for train in trains:
            if (time.strptime(time.strftime('%H%M'), '%H%M') == train.arrive_time) and (train not in self.arrived_trains):
                for way in self.ways:
                    if train.capacity <= way.capacity and way.filling is None \
                            and (s_ways is None or s_ways.capacity > way.capacity):
                        s_ways = way

                if s_ways is not None:
                    s_ways.filling = train
                    self.arrived_trains.append(train)
                    trains.remove(train)

                    return 'Поезд {train_name} занял линию {name}'.format(name=s_ways.name,
                                                                          train_name=s_ways.filling.name)

                elif sorted(self.ways, key=lambda way: way.capacity, reverse=True)[0] < train.capacity:
                    print('Поезд {} не заехал на станцию'.format(train.name))
                    trains.remove(train)
            return None

    def out_fill(self, trains):
        for train in trains:
            if (time.strptime(time.strftime('%H%M'), '%H%M') == train.out_time) and \
               (train in self.arrived_trains):
                for way in self.ways:
                    if way.filling is None:
                        continue
                    elif way.filling.name == train.name:
                        out = 'Поезд {train_name} покинул линию {name}'.format(name=way.name,
                                                                               train_name=way.filling.name)
                        self.arrived_trains.remove(train)
                        way.filling = None
                        return out
            return None
