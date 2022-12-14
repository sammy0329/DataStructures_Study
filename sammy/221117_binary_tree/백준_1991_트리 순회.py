class Node():
    def __init__(self,item,left,right):
        self.item=item
        self.left=left
        self.right=right


def preorder(node):

    print(node.item,end='')
    if node.left!='.':
        preorder(dataset[node.left])
    if node.right!='.':
        preorder(dataset[node.right])


def postrorder(node):
   
    if node.left!='.':
        postrorder(dataset[node.left])
    if node.right!='.':
        postrorder(dataset[node.right])
    print(node.item,end='')

def inorder(node):
   
    if node.left!='.':
        inorder(dataset[node.left])
    print(node.item,end='')
    if node.right!='.':
        inorder(dataset[node.right])
    
n=int(input())
dataset=dict()

for i in range(n):
    parent,left,right=map(str,input().split())
    dataset[parent]=Node(parent,left,right)



preorder(dataset['A'])
print()
inorder(dataset['A'])
print()
postrorder(dataset['A'])
