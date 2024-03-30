import difflib

class CodeCommit(Commit):
    ...

    def compare(self, other_commit,graph):
        if self.commit_name == other_commit.commit_name:
            print("Nema promena.")
            return

        pre_change_commit= from_commit(graph)
        post_change_commit= self

        pre_changes = graph.nodes[pre_change_commit.commit_name].changes
        post_changes = graph.nodes[post_change_commit.commit_name].changes

        differences = difflib.unified_diff(
            [str(change) for change in pre_changes],
            [str(change) for change in post_changes],
            lineterm=''
        )

        print('\n'.join(differences))

def from_commit(self, graph):
    current_commit = self
    while current_commit.parent_id:
        if current_commit.parent_id in graph.nodes:
            current_commit = graph.nodes[current_commit.parent_id]
            return graph.nodes[current_commit.parent_id]
        current_commit = graph.nodes[current_commit.parent_id]
    raise ValueError("Nije pronađen prethodni commit u grafu.")
   







