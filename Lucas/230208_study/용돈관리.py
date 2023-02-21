input = __import__('sys').stdin.readline
n, m = map(int, input().split())
budget = [int(input()) for i in range(n)]
lo = min(budget)
hi = sum(budget)
ans = 0
 
while lo <= hi:
    mid = (lo + hi) // 2
 
    total = 0
    count = 0
    for today in budget:
        if total < today:
            total = mid
            count += 1
        total -= today
 
    if count > m or mid < max(budget):
        lo = mid + 1
    else:
        hi = mid - 1
        ans = mid
 
print(ans)