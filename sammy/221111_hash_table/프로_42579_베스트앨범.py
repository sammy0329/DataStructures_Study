from heapq import heappush,heappop,heapify

def solution(genres, plays):
    answer = []
    dataset={}
    total={}
    for i in range(len(genres)):
        if genres[i] not in dataset:
            dataset[genres[i]]=[(-plays[i],i)]
            total[genres[i]]=plays[i]
        else:
            dataset[genres[i]].append((-plays[i],i))
            total[genres[i]]+=plays[i]

    heap=[]
    for key,value in total.items():
        heappush(heap,(-value,key)) 
        heapify(dataset[key])

    length=len(heap)
    for i in range(length):
        data=heappop(heap)[1]
        if len(dataset[data])==1: answer.append(heappop(dataset[data])[1])
        else:
            for j in range(2):
                answer.append(heappop(dataset[data])[1])
    return answer