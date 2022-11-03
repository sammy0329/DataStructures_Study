import sys
N,P=map(int,sys.stdin.readline().split())
dic={1:[],2:[],3:[],4:[],5:[],6:[]}
cnt=0


for i in range(N):
    line,plet=map(int,sys.stdin.readline().split())
    if dic[line]:
        if dic[line][-1]==plet: pass
        
        elif dic[line][-1]<plet:
            cnt+=1
            dic[line].append(plet)
            
        else:
            for i in range(len(dic[line])+1):
                
                if not dic[line]:
                    dic[line].append(plet)
                    cnt+=1
                    break
                
                if dic[line][-1]<plet:
                    dic[line].append(plet)
                    cnt+=1
                    break
                
                elif dic[line][-1]==plet:
                    break

                cnt+=1
                dic[line].pop()
    else:
        cnt+=1
        dic[line].append(plet)

    # print(dic[line],cnt)
print(cnt)                