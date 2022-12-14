import sys

#회전 후의 행 번호 = 회전 전의 열 번호
#회전 후의 열 번호 = N - 1 - 회전 전의 행 번호
def rotate(data):
    n = len(data)
    m = len(data[0])
    new = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            new[j][n-i-1] = data[i][j]
    return new


def solution():
    n=int(sys.stdin.readline())
    data=[list(map(str, input().split())) for _ in range(n)]
    cnt=0
    count=[]

    all=[]

    for i in range(n):
        idx1=None
        idx2=None
        li=[]
        for j in range(n):
            if data[i][j]=='S':
                idx1=j
                if idx2!=None and idx2>idx1:
                    if idx2-idx1==1: return 'NO'
                    for k in range(idx1+1,idx2):
                        
                        li.append((i,k))
  
                    count.append(li)
                    all.extend(li)
                    li=[]
                        
                elif idx2!=None and idx2<idx1:
                    if idx1-idx2==1: return 'NO'
                    for k in range(idx2+1,idx1):
        
                        li.append((i,k))
        
                        
                    count.append(li)
                    all.extend(li)
                    li=[]                        
            elif data[i][j]=='T':
                idx2=j
                
                if idx1!=None and idx2<idx1:
                    
                    if idx1-idx2==1: return 'NO'
                    
                    for k in range(idx2+1,idx1):
                        li.append((i,k))
                 
                    count.append(li)
                    all.extend(li)
                    li=[]                    
                elif idx1!=None and idx2>idx1:
                    
                    if idx2-idx1==1: return 'NO'
                    
                    for k in range(idx1+1,idx2):
                        li.append((i,k))
                    count.append(li)
                    all.extend(li)
                    li=[]                        


    reverse_data=rotate(data)

    for i in range(n):
        idx1=None
        idx2=None
        li=[]
        for j in range(n):
            if reverse_data[i][j]=='S':
                idx1=j
                # if reverse_data[i][j+1]=='T': return False
                
                if idx2!=None and idx2>idx1:
          
                    if idx2-idx1==1: return 'NO'
                    for k in range(idx1,idx2-1):
                   
                        li.append((n-k-2,i))
                      
                    count.append(li)
                    all.extend(li)
                    li=[]  
                elif idx2!=None and idx2<idx1:
         
                    if idx1-idx2==1: return 'NO'
                    for k in range(idx2,idx1-1):
       
                        li.append((n-k-2,i))
                      
                    count.append(li)
                    all.extend(li)
                    li=[]                      
            elif reverse_data[i][j]=='T':
                idx2=j
                
                if idx1!=None and idx2<idx1:
                  
                    if idx1-idx2==1: return 'NO'
                    
                    for k in range(idx2,idx1-1):
                        li.append((n-k-2,i))
                      
                    count.append(li)
                    all.extend(li)
                    li=[]      
                                       
                elif idx1!=None and idx2>idx1:
                 
                    if idx2-idx1==1: return 'NO'
                    
                    for k in range(idx1,idx2-1):
                        li.append((n-k-2,i))
                    
                    count.append(li)
                    all.extend(li)
                    li=[]                       

    
    all_count = {} # 각 원소의 등장 횟수를 카운팅할 딕셔너리

    for i in all:
        try: # 이미 등장한 값의 경우
            all_count[i] += 1
        except: # 처음 등장한 값의 경우
            all_count[i] = 1



    for check in set(all):
        if all_count[check]>1:           
            cnt+=1
            for i in range(len(count)):
                if check in count[i]:
                    count[i].clear()
           

    
    for i in range(len(count)):
        if count[i]:
            cnt+=1
            
    # print(count,cnt)             
    if cnt<=3: return 'YES'
    else: return 'NO'

print(solution())
                
# T X X S X T
# X X S S X X
# X X X X T X
# X X S S X S
# X X X X X X
# S X X X X X
                
# 반례
# 5
# X X S X X
# X X X X X
# S X T X S
# X X X X X
# X X S X X


            
# 4
# X S X T
# X X S X
# X X X X
# T T T X

# Yes

# --------------------------------------------------------------------------------

# 5
# X X S X X
# X X X X X
# S X T X S
# X X X X X
# X X S X X

# NO

# --------------------------------------------------------------------------------

# 5
# X T X T X
# T X S X T
# X S S S X
# T X S X X
# X T X X X

# YES

# --------------------------------------------------------------------------------

# 5
# X S S S X
# T X X S X
# X T X S X
# X X T X S
# X X X T X

# Yes