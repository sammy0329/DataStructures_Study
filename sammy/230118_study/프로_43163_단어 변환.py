count = 0
min_count=[]
checked_word=[]

def back(word,target,words):
    global count
    
    if word==target:
        # print(checked_word)
        min_count.append(count)
        return
    
    for check in words:
        # print((word,check),len(set(word)-set(check)))
        if check not in checked_word:
            cnt=0
            
            for idx in range(len(check)):
                if check[idx]!=word[idx]: cnt+=1
                
            
            if cnt==1:  
                
                checked_word.append(check)
                count+=1
                back(check,target,words)
                checked_word.pop()
                count-=1
            
    

def solution(begin, target, words):

    
    if target not in words:
        return 0
    
    back(begin,target,words)
    print(min_count)
    if min_count:
        return min(min_count)
    else:
        return 0

# print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
# print(solution("hit", "cog", ["cog", "log", "lot", "dog", "dot", "hot"]))
# print(solution("hit","cog",["hot", "dot", "dog", "lot", "log"]))
print(solution("hhf","hih",["hih"]))