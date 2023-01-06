def solution(survey, choices):
    answer = ''
    result = [0,0,0,0]
    liss = ["R","T","C","F","J","M","A","N"]
    a = 0
    for i in range(len(survey)):
        
        if(survey[i] == "RT" or survey[i] == "TR"):
            
            if(survey[i] == "RT"):
                result[0] += (choices[i]-4)
                
            else:
                result[0] -= (choices[i]-4)
                
        elif(survey[i] == "CF" or survey[i] == "FC"):
            
            if(survey[i] == "CF"):
                result[1] += (choices[i]-4)
                
            else:
                result[1] -= (choices[i]-4)
                
        elif(survey[i] == "JM" or survey[i] == "MJ"):
            
            if(survey[i] == "JM"):
                result[2] += (choices[i]-4)
                
            else:
                result[2] -= (choices[i]-4)
                
        else:
            
            if(survey[i] == "AN"):
                result[3] += (choices[i]-4)
                
            else:
                result[3] -= (choices[i]-4)
    for i in result:
        
        if(i<=0):
            answer = answer + liss[a]
        else:
            answer = answer + liss[a+1]
            
        a+=2
    return answer
    
survey = ["TR", "RT", "TR"]
choices = 	[7, 1, 3]
solution(survey, choices)