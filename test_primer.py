from commit import *
from codeCommit import *
from change import *
from management import *

commit = CodeCommit(0)
projekat = Management(commit)

commit1 = CodeCommit(1, projekat.head.commit_name)
commit1.add_change(Add('print ("Hello")'))

commit2 = CodeCommit(2, projekat.head.commit_name)
commit2.add_change(Add('a = input()'))
commit2.add_change(Add('b = input()'))
projekat.addCommit(commit2)

commit3 = CodeCommit(3, projekat.head.commit_name)
commit3.add_change(Add('c = a + b'))
projekat.addCommit(commit3)

commit4 = CodeCommit(4, projekat.head.commit_name)
commit4.add_change(Add('print(c)'))
projekat.addCommit(commit4)

projekat.setHead(3)
print(projekat.head.commit_name)

commit5 = CodeCommit(5, projekat.head.commit_name)
commit5.add_change(Modifikacija('c = a * b'))
projekat.addCommit(commit5)

projekat.log()
