import sys
N,P=map(int,sys.stdin.readline().split())

stack=[]
finger=[]
current_line=0
current_max=-9999
cnt=0


for i in range(N):
    line,plet=map(int,sys.stdin.readline().split())
    stack.append((line,plet))
stack.reverse()
# 기타줄에 따라 판단하기 편하게 하기 위해 앞에꺼 기준 sort 진행
stack.sort(key=lambda stack: stack[0])
print(stack)
# while stack:

#     data=stack.pop()
#     if data[0]!=current_line:
#         cnt+=1
        
#         current_line=data[0]
#         current_max=data[1]

#         finger=[]
#         finger.append(data[1])
        
#     else:
#         if current_max==data[1]: pass
        
#         elif data[1]>current_max:
#             current_max=data[1]
#             cnt+=1
#             # if data[1] not in fingercount:
#             finger.append(data[1])
            
#         else:

#             for i in range(len(finger)):
                
#                 if finger[-1]==data[1]:
#                     break
                
#                 elif finger[-1]<data[1]:
#                     cnt+=1
#                     finger.append(data[1])
#                     break
                
#                 else:
#                     finger.pop()
#                     cnt+=1

#     # print(stack,finger,cnt)
# print(cnt+1)
                    
                
            
        
        

   