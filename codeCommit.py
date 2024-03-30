from commit import *


class CodeCommit(Commit):

    def __init__(self, commit_name, parent=None): 
        self.commit_name = commit_name
        self.parent_id = parent
        self.children_id = []
        self.changes = []

    def get_changes(self):
        return self.changes

    def add_change(self, change):
        self.changes.append(change) 

    def logCommit(self):
        print(f"Commit ID: {self.commit_name}")
        print("Changes:")
        for change in self.changes:
            print(change)



   