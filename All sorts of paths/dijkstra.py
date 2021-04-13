nodes = []

class node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.edges = []
        self.shortest_distance = float('inf')
        self.shortest_path_via = None

        nodes.append(self)

    def add_edge(self, node, distance):
        self.edges.append([node, distance])

    def update_edges(self):
        for edge in self.edges:
            distance_via = self.shortest_distance + edge[1]
            if distance_via < edge[0].shortest_distance:
                edge[0].shortest_distance = distance_via
                edge[0].shortest_path_via = self

# Couples two nodes
def make_edge(node1, node2, distance):
    node1.add_edge(node2, distance)
    node2.add_edge(node1, distance)

# Does the heavy lifting
# Just a python implementation of dijkstras shortest path
def dijkstra(start, end):
    global nodes
    queue = []
    path = []

    queue = nodes.copy()
    start.shortest_distance = 0
    queue.sort(key=lambda node: node.shortest_distance)

    while queue[0] != end:
        node = queue[0]
        node.update_edges()
        path.append(queue.pop(0))
        queue.sort(key=lambda node: node.shortest_distance)
    
    print(print_path(end))
    print(f"Distance: {end.shortest_distance}")

# Literally just prints the path
def print_path(node):
    if node.shortest_path_via == None:
        return f"{node.symbol}"
    else:
        return f"{print_path(node.shortest_path_via)} -> {node.symbol}"

# Does what it says on the tin
def get_node(symbol):
    for node in nodes:
        if node.symbol == symbol:
            return node
    return 0

# Takes a set of edges, as well as start and end nodes
def solve_dijkstra(edges, start, end):
    # Make edges into nodes and couple them
    for edge in edges:
        a = get_node(edge[0])
        b = get_node(edge[1])

        if a == 0:
            a = node(edge[0])

        if b == 0:
            b = node(edge[1])

        a.add_edge(b, edge[2])
        b.add_edge(a, edge[2])

    # Solve path
    dijkstra(get_node(start), get_node(end))


data = [
    ["A", "B", 3],
    ["A", "C", 1],
    ["D", "B", 1],
    ["C", "B", 1],
    ["D", "E", 1],
    ["B", "E", 3],
    ["C", "D", 3],
]
solve_dijkstra(data, "A", "E")