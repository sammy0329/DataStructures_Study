def solution(numbers, target):
    answer = 0
    graph= [0]
    for i in numbers:
        result = []
        for j in graph : 
            result.append(j+i)
            result.append(j-i)
        graph = result
    answer=graph.count(target)
    return answer