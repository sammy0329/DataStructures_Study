#%%
import numpy as np

def solution(scores):
    answer = 1
    young = np.array(scores[0])
    scores = sorted(scores,key = lambda x : (x[0],x[1]))

    for i in range(len(scores)):
        
        scores[i] = np.array(scores[i])

    for i in range(len(scores)):##인센티브 못받는 놈들 제거 시간복잡도 N**2
        
        cmp1 = scores[i]
        
        for j in range(len(scores)-1,i,-1):
            if(scores[j][0] == scores[i][0]):
                continue
                
            cmp2 = scores[j]
                
            if(cmp1<cmp2).all():
                scores[i] = np.array([-1,-1])
                break

    for i in range(len(scores)):
        if(scores[i] == np.array([-1,-1])).all():
            continue
        cmp = scores[i]
        
        if sum(cmp) > sum(young): ##석차 체크
            
            answer += 1
            
        if(young<cmp).all():
            
            return -1
    return answer

solution([[2,2],[1,4],[3,2],[3,2],[2,1]])

# %%
# import numpy as np

# def binary_search(num,goal,scores):
#     right = len(scores)
#     left = num

#     for i in range(num+1,len(scores)):

#         if(scores[i][0] == goal[0]):
#             print(scores[i][0])
#             continue
#         left = i
#         break

#     scores = sorted(scores[left:right],key = lambda x : x[1])

#     if goal[1] < scores[len(scores)-1][1]:
#         return True
#     else:
#         return False


# def solution(scores):
#     answer = 1
#     young = np.array(scores[0])
#     scores = sorted(scores,key = lambda x : x[0])

#     for i in range(len(scores)):
        
#         scores[i] = np.array(scores[i])

#     for i in range(len(scores)):##인센티브 못받는 놈들 제거 시간복잡도 N**2
#         a = binary_search(i,scores[i],scores)
#         if a:
#             scores[i] = np.array([-1,-1])


#     for i in range(len(scores)):
#         if(scores[i] == np.array([-1,-1])).all():
#             continue
#         cmp = scores[i]
        
#         if sum(cmp) > sum(young): ##석차 체크
            
#             answer += 1
            
#         if(young<cmp).all():
            
#             return -1
#     return answer
# solution([[4, 1], [2, 4], [3, 5]])
# # %%
# a = [1,2,3,4]
# a[3:3]
# %%
