class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node):
        if node not in self.nodes:
            self.nodes[node] = []

    def add_edge(self, node1, node2):
        if node2 not in self.nodes[node1]:
            self.nodes[node1].append(node2)
            self.nodes[node2].append(node1)

    def remove_node(self, node):
        for k in self.nodes[node]:
            self.cvorovi[k].remove(node)
        del self.cvorovi[node]
    
    def remove_edge(self, node1, node2):
        self.cvorovi[node1].remove(node2)
        self.cvorovi[node2].remove(node1)


        