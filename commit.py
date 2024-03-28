from abc import ABC, abstractclassmethod

class Commit(ABC):

    @abstractclassmethod
    def add_change(self, change):
       ...

    @abstractclassmethod
    def log(self):
       ...
