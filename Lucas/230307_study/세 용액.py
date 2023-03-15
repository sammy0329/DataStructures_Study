N = int(input())

liquid = list(map(int,input().split(" ")))
liquid = sorted(liquid)

def binary_search(x,y,liquid):
    
    left = x+1
    right = y-1
    ans = (left + right) // 2
    while left <= right:
        
        mid = (left + right) // 2
        if abs(liquid[x]+liquid[mid]+liquid[y])<abs(liquid[x]+liquid[ans]+liquid[y]):
            ans = mid
        if liquid[x]+liquid[mid]+liquid[y] > 0:
            
            right = mid - 1

        elif liquid[x]+liquid[mid]+liquid[y] < 0:

            left = mid + 1

        else:
            return [liquid[x],liquid[mid],liquid[y]]
    if(x == y or x == ans or y== ans):
        return 0
    return [liquid[x],liquid[ans],liquid[y]]
ans = [-10000000000,0,0]

x=0
y=0

while True:
    if(x == len(liquid)-1):
        break
    y+=1
    result = binary_search(x,y,liquid)
    if(y>=(len(liquid)-1)):
        x+=1
        y = x
    if result == 0:
        continue
    if abs(sum(ans))>abs(sum(result)):
        ans = result

print(*ans)