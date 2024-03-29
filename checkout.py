from commit import *
from pomeranje_head import *
from change import *
from comapre import *

class Graph:
    ...

    def checkout(self, commit_id):
        if commit_id not in self.nodes:
            print("Commit nije pronađen u grafu.")
            return

        current_commit = self.nodes[commit_id]
        code_state = {}

        while current_commit:
            for change in current_commit.changes:
                if isinstance(change, Add):
                    code_state[change.number] = change.content
                elif isinstance(change, Delete):
                    if change.number in code_state:
                        del code_state[change.number]
                elif isinstance(change, Modifikacija):
                    if change.number in code_state:
                        code_state[change.number] = change.content

            current_commit = self.get_parent_commit(current_commit)

        print("Konačno stanje koda:")
        for number, content in code_state.items():
            print(f"Linija {number}: {content}")

    def get_parent_commit(self, commit):
        if commit.parent_id in self.nodes:
            return self.nodes[commit.parent_id]
        return None
