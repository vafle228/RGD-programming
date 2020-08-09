from functions import valid


class Way:
    def __init__(self, capacity, name, train=None):
        self.capacity = valid(capacity, 'int')
        self.name = name
        self.filling = train


class Train:
    def __init__(self, capacity, name, arrive_time, out_time):
        self.capacity = valid(capacity, 'int')
        self.name = valid(name, 'train_name')
        self.arrive_time = valid(arrive_time, 'time')
        self.out_time = valid(out_time, 'time')
