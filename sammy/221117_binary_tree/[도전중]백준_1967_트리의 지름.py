class Node():
    def __init__(self,parent,child,weight):
        self.parent=parent
        self.child=child
        self.weight=weight

n=int(input())
dataset=dict()

for i in range(n-1):
    parent,child,weight=map(int,input().split())
    if str(parent) in dataset:
        dataset[str(parent)].append(Node(parent,child,weight))
    else:
        dataset[str(parent)]=[Node(parent,child,weight)]


    
print(dataset)