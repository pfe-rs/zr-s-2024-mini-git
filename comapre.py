import difflib

class CodeCommit(Commit):
    ...

    def compare(self, other_commit):
        if self.commit_name == other_commit.commit_name:
            print("Nema promena.")
            return

        pre_change_file = load_from_commit(self.parent_id)
        post_change_file = load_from_commit(self.commit_name)

        differences = difflib.unified_diff(
            pre_change_file.splitlines(),
            post_change_file.splitlines(),
            lineterm='',
            fromfile='Pre promena',
            tofile='Posle promena'
        )

        print('\n'.join(differences))

def load_from_commit(commit_id):
   
    pass




