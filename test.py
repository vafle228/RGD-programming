class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        self.graph[node] = {}

    def add_relation(self, current_node, node, value):
        self.graph[current_node][node] = value


def create_costs(graph):
    costs = {}
    for node in list(graph.keys())[1::]:
        if node in list(graph[list(graph.keys())[0]].keys()):
            costs[node] = graph[list(graph.keys())[0]][node]
        else:
            costs[node] = float('inf')
    return costs


def create_parents(graph):
    parents = {}
    for node in list(graph.keys())[1::]:
        if node in list(graph[list(graph.keys())[0]].keys()):
            parents[node] = list(graph.keys())[0]
        else:
            parents[node] = None
    return parents


def find_lowest_cost_node(costs, processed):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


def dijkstra(graph, start, finish):
    processed = []
    costs = create_costs(graph)
    parents = create_parents(graph)
    node = find_lowest_cost_node(costs, processed)

    while node is not None:
        cost = costs[node]
        neighbors = graph[node]

        for key in neighbors.keys():
            new_cost = cost + neighbors[key]
            if costs[key] > new_cost:
                costs[key] = new_cost
                parents[key] = node

        processed.append(node)
        node = find_lowest_cost_node(costs, processed)
    return format_dijkstra_out(parents, costs[list(graph.keys())[-1]], start, finish)


def format_dijkstra_out(parents, final_cost, start, finish):
    node = finish
    data = []
    while node != start:
        data.append(node)
        node = parents[node]
    data.append(start)
    for node in data[::-1]:
        if node == data[0]:
            print('{node}'.format(node=node))
        else:
            print('{node} -> '.format(node=node), end='')
    return 'Всего потребуется {final_cost} времени'.format(final_cost=final_cost)


def create_graph(nodes, relations, graph):
    for node in nodes:
        graph.add_node(node[0])

    last_relations = [None, None]
    for relation in relations:
        if (relation[0] == last_relations[1]) and (relation[1] == last_relations[0]):
            continue
        graph.add_relation(relation[0], relation[1], relation[2])
        last_relations = [relation[0], relation[1]]
    return graph.graph
