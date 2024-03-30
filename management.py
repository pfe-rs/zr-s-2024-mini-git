from commit import *
from codeCommit import *
from change import *

class Management():

    def __init__(self, rootCommit):
        self.root = rootCommit #pocetni commit
        self.head = rootCommit #u pocetku je head na root
        self.commits = [] #vec je graf jer commit ima parent
        self.commits.append(rootCommit)

    def addCommit(self, commit): #dodaje commmit u graf
        self.commits.append(commit)
        self.head = commit
        self.commits[commit.parent_id].children_id.append(commit.commit_name) #omogucava dodavanje vise dece

    def setHead(self, commit_id): #setuje head na odredjeni commit, ako taj commit id postoji
        
        for commit in self.commits:
            if commit_id == commit.commit_name:  # ovo nece da izbaci gresku
                self.head = self.commits[commit_id]
            return True
        raise ValueError("ne postoji head sa tim commit_id")  
        

    def getHead(self): #vraca trenutni head
        return self.head

    def log(self): #print graf

        for commit in self.commits:
            commit.logCommit()

