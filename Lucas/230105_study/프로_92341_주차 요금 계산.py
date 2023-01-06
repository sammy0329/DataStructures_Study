#%%
def solution(fees, records):
    answer = []
    dic  = {}
    fee = {}
    checkout = {}
    for i in records:
        time,car,inout=i.split(" ")
        car = int(car)
        if(inout == "IN"):
            dic[car] = time
            checkout[car] = 1
            if(car not in fee):
                fee[car] = 0
                
        else:
            checkout[car] = 0
            in_h,in_m = map(int,dic[car].split(":"))
            out_h,out_m = map(int,time.split(":"))
            
            diff = (60-in_m)+((out_h-(in_h+1))*60) + out_m

            fee[car] += diff
    
    for i in checkout:
        if(checkout[i] == 1):
            time = "23:59"
            car = i
            in_h,in_m = map(int,dic[car].split(":"))
            out_h,out_m = map(int,time.split(":"))
            
            diff = (60-in_m)+((out_h-(in_h+1))*60) + out_m
            fee[car] += diff
    print(fee)
    for i in fee:
        if(fee[i]<=fees[0]):
            fee[i] = fees[1]
        else:
            
            a = ((fee[i]-fees[0])//fees[2])*fees[3]
            if(fee[i]-fees[0])%fees[2] != 0:
                b = fees[3]
                fee[i] = a+b+fees[1]
                continue
            fee[i] = a + fees[1]
    fee = dict(sorted(fee.items()))
    answer = list(fee.values())
    
    return answer
fees = [120, 0, 60, 591]
records = ["16:00 3961 IN","16:00 0202 IN","18:00 3961 OUT","18:00 0202 OUT","23:58 3961 IN"]

solution(fees,records)
# %%
(334-180)%10 != 0
# %%
