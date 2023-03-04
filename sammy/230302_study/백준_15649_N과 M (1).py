import sys
from itertools import permutations

# 백트래킹 활용한 문제풀이
input = sys.stdin.readline

n,m = list(map(int,input().split()))
 
ouput = []
 
def backtracking():
    if len(ouput)==m:
        print(' '.join(map(str,ouput)))
        return
    
    for i in range(1,n+1):
        if i not in ouput:
            ouput.append(i)
            backtracking()
            ouput.pop()
 
backtracking()

# input=sys.stdin.readline

# n,m = map(int,input().split())

# for check in permutations(range(1,n+1),m):
#     for i in range(len(check)):
#         print(str(check[i]),end=" ")
#     print()