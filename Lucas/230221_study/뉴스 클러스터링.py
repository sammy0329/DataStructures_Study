def solution(str1, str2):
    result1 = [(str1[i:i+2]).lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    result2 = [(str2[i:i+2]).lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]
    cnt1=0
    cnt2=0
    
    if result1==result2:
        return 65536
    for i in result1:
        if i in result2:
            result2.remove(i)
            cnt1+=1
    cnt2=len(result1+result2)

    return int((cnt1/cnt2)*65536)