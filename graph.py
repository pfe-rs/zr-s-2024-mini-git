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

    def move_head(self, new_head):
        if new_head in self.nodes:
            self.head = new_head
            
        else:
            print(f"Čvor {new_head} ne postoji u grafu.")

    def move_head_command(self):
        new_head = input("Unesite ime čvora na koji želite da pomerite HEAD: ")
        self.move_head(new_head)
        print(f"HEAD je sada pomeren na čvor {new_head}.")
 
    def move_head_relative(self, delta):
        if self.head is None:
            return

        current_index = list(self.nodes.keys()).index(self.head)
        new_index = current_index + delta

        if 0 <= new_index < len(self.nodes):
            new_head = list(self.nodes.keys())[new_index]
            self.head = new_head
            print(f"HEAD je pomeren za {delta} čvorova. Novi HEAD je na čvoru {new_head}.")
        else:
            print("Nije moguce pomeranje van granica grafa.")
        