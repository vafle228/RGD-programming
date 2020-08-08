import time


class Way:
    def __init__(self, capacity, name, train=None):
        self.capacity = valid(capacity, 'int')
        self.name = name
        self.filling = train


class Train:
    def __init__(self, capacity, name, arrive_time, out_time):
        self.capacity = valid(capacity, 'int')
        self.name = name
        self.arrive_time = valid(arrive_time, 'time')
        self.out_time = valid(out_time, 'time')


def valid(data, p_type):
    data = str(data)
    if p_type == 'int':
        if data.isdigit() and int(data) > 0:
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
