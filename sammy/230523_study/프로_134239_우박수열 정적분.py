def checkSuyol(x):
    xyData=[x]
    while x>1:
        if x % 2 == 0:
            x/=2
        else:
            x=x*3+1
        xyData.append(x)
    return xyData


def solution(k, ranges):
    answer = []
    xyData=checkSuyol(k)

    for checkRange in ranges:
        total=0

        if checkRange[0]+abs(checkRange[1])>len(xyData)-1:
            total=-1.0

        else:
            for i in range(checkRange[0],len(xyData)+checkRange[1]-1):
                total+=(xyData[i+1]-xyData[i])/2
                total+=xyData[i]

        answer.append(total)

    return answer

print(solution(5,[[0,0],[0,-1],[2,-3],[3,-3]]),[33.0,31.5,0.0,-1.0])