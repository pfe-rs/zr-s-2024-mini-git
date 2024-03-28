from commit import *


class CodeCommit(Commit):

    def __init__(self, commit_name, parent=None):
        super().__init__(commit_name, parent)
        self.changes = []

    def add_change(self, change):
        self.changes.append(change)

    def log(self):
        print(f"Commit ID: {self.commit_name}")
        print("Changes:")
        for change in self.changes:
            print(change)
   