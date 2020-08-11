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
        if node in list(graph['start'].keys()):
            costs[node] = graph['start'][node]
        else:
            costs[node] = float('inf')
    return costs


def create_parents(graph):
    parents = {}
    for node in list(graph.keys())[1::]:
        if node in list(graph['start'].keys()):
            parents[node] = 'start'
        else:
            parents[node] = None
    return parents
    
def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node

def dijkstra(costs, parents, graph):
    processed = []
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

    return parents, cost, graph


parents = create_parents(graph.graph)
costs = create_costs(graph.graph)

print(dijkstra(costs, parents, graph.graph))

