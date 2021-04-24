# It make a node
class node:
    def __init__(self, symbol):
        self.symbol = symbol
        self.edges = []
        self.shortest_distance = float('inf')
        self.shortest_path_via = None

    # Adds another node as a weighted edge
    def add_edge(self, node, distance):
        self.edges.append([node, distance])


def make_nodes(edge_data, *args):
    """
    Takes an array of edges and makes them into node objects.

    PARAMS:
        edge_data (arr): array of edges with format [start_node (str), end_node (str), distance (int)]
        *args (boolean): True if you want digraph, False if not (default is True) Can save time when entering edges by hand.
        *args (array[str]): array of symbols to use for nodes that may not have edges and are not included in "edge_data"
    RETURNS:
        array: array of the nodes that it created
    """

    nodes = []

    # Decide if digraph or not
    if len(args) > 0:
        digraph = args[0]
        print(f"Digraph setting {digraph}")
    else:
        digraph = False

    # Fill in empty nodes
    if len(args) > 1:
        for symbol in args[1]:
            nodes.append(node(symbol))

    # Make edges into nodes and couple them
    for edge in edge_data:
        node1 = get_node(nodes, edge[0])
        node2 = get_node(nodes, edge[1])

        if node1 == None:
            node1 = node(edge[0])

        if node2 == None:
            node2 = node(edge[1])

        node1.add_edge(node2, edge[2])
        if not digraph: node2.add_edge(node1, edge[2])  # REMOVE THIS IF YOU WANT DIGRAPH 2/2
    
        if node1 not in nodes: nodes.append(node1)
        if node2 not in nodes: nodes.append(node2)

    return nodes


def get_node(nodes, symbol):
    """
    Searches "nodes" for node with symbol "symbol" and returns it if found.

    PARAMS:\n
        nodes (array): array of nodes to search from
        symbol (str): string to search matches for
    RETURNS:\n
        node: if match is found
        None: if no match found
    """

    for node in nodes:
        if node.symbol == symbol:
            return node
    return None


def bellman_ford(nodes, edge_count, start):
    """
    Takes an array of nodes, and finds the shortest distance from "start" to each of them

    PARAMS:
        nodes (array[node]): array of the relevant nodes
        edge_count (int): number of edges (not nodes)
        start (node): starting node to search from
    
    RETURNS:
        array[node]: array of the nodes sorted by ascending distance to "start"
    """

    start.shortest_distance = 0
    
    for i in range(edge_count):
        for node in nodes:
            for edge in node.edges:
                if node.shortest_distance + edge[1] < edge[0].shortest_distance:
                    edge[0].shortest_distance = node.shortest_distance + edge[1]
                    edge[0].shortest_path_via = node

    nodes.sort(key=lambda x: x.shortest_distance)

    return nodes