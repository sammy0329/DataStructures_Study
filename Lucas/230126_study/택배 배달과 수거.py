#%%
def solution(cap, n, deliveries, pickups):
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    deli = 0
    pick = 0
    for i in range(n):
        deli += deliveries[i] # 배송일
        pick += pickups[i] #수거일

        print(deli)
        print(pick)

        while deli > 0 or pick > 0:
            deli -= cap
            pick -= cap
            answer += (n - i) * 2
            print(answer)
            
    return answer
#%%
solution(4,5,[1,0,3,3,2],[0,3,0,4,0])
#%%