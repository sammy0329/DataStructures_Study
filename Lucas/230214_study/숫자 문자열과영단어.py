#%%
def solution(s):
    answer = ""
    words = {"zero":"0","one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
    queue = ""
    for i in s:
        if(queue in words):
            answer+=words[queue]
            queue = ""
        try:
            a = int(i)

            if(queue !=""):
                answer+=words[queue]
                
            answer+=i
            queue = ""
        except:

            queue += i

    if(queue != ""):
        answer+=words[queue]      
    return int(answer)
#%%