import sys

def backTracking(n,total):
    
    global count
    
    if total>n: return # total 값이 n보다 클 경우 종료 조건
    
    if total==n: # total 값이 n일 경우 count+1을 해주고 종료
        count+=1
        return
    
    for i in range(1,4): # 1부터 3까지의 수들로 합을 만들기
        total+=i
        backTracking(n,total)
        total-=i
    
input = sys.stdin.readline
T=int(input())

for tc in range(1,T+1):
    count=0
    backTracking(int(input()),0)
    print(count)
