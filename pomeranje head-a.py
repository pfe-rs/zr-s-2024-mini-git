    
class Graph():
    ...
    def move_head(self, new_head):
        if new_head in self.nodes:
            self.head = new_head
       
        else:
         return
 
    def move_head(self, new_head):
        try:
            if new_head not in self.nodes:
                raise ValueError(f"Čvor {new_head} ne postoji u grafu.")

            self.head = new_head
        except ValueError as e:
            ...

    def move_head_relative(self, delta):
        if self.head is None:
            return

        current_index = list(self.nodes.keys()).index(self.head)
        new_index = current_index + delta

        if 0 <= new_index < len(self.nodes):
            new_head = list(self.nodes.keys())[new_index]
            self.head = new_head
            return
        else:
            return