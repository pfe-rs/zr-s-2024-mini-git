from abc import ABC, abstractmethod

class Commit(ABC):

    @abstractmethod
    def __init__(self, commit_name, parent=None):
        self.commit_name = commit_name
        self.parent_id = parent
        self.changes = []

    def add_change(self, change):
       ...

    def log(self):
       ...