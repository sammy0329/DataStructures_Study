import sys
from itertools import combinations

# 백트래킹으로 문제풀이
input = sys.stdin.readline

n,m = list(map(int,input().split()))
 
ouput = []
 
def backtracking():
    if len(ouput)==m:
        print(' '.join(map(str,ouput)))
        return
    
    for i in range(1,n+1):
        if not ouput: 
            ouput.append(i)
            backtracking()
            ouput.pop()
        else:    
            if i not in ouput and i>ouput[-1]:
                ouput.append(i)
                backtracking()
                ouput.pop()
 
backtracking()


# combinations 활용 문제풀이

# input=sys.stdin.readline

# n,m = map(int,input().split())

# for check in combinations(range(1,n+1),m):
#     for i in range(len(check)):
#         print(str(check[i]),end=" ")
#     print()