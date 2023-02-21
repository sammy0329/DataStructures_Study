import sys
input = sys.stdin.readline

N , M = map(int,input().rstrip().split())

Z = (M *100)//N
ans = 0
if Z >= 99:
    print(-1)
else:
    ans = 0
    start =1
    end = N
    while start <= end:
        mid = (start+end)//2
        if (M+mid)*100 // (N+mid) > Z:
            ans = mid
            end = mid -1
        else:
            start = mid+1
    print(ans)