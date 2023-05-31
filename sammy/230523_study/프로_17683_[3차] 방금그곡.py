def changeShap(music): # "#"이 붙은 음을 소문자로 변환하는 함수
    music = music.replace('A#', 'a').replace('F#', 'f').replace('C#', 'c').replace('G#', 'g').replace('D#', 'd')
    return music

def solution(m, musicinfos):
    answer = []
    idx=0  # 음악 순서를 나타내는 변수
    m=changeShap(m) # '#'이 붙은 음을 소문자로 변환

    for info in musicinfos:
        check='' # 재생된 음 저장하는 변수
        idx+=1
 
        startTime,endTime,music,sound=info.split(',') # ','로 split

        # 시간을 분으로 계산해서 얼마나 재생됐는지 파악
        endTime=int(endTime.split(':')[0])*60+int(endTime.split(':')[1])
        startTime=int(startTime.split(':')[0])*60+int(startTime.split(':')[1])
        totalTime=endTime-startTime

        sound=changeShap(sound)  # '#'이 붙은 음을 소문자로 변환

        # 재생된 음 저장
        check+=sound*(totalTime//len(sound))
        check+=sound[:(totalTime%len(sound))]
        
        if m in check: # m의 값이 재생된 음에 있으면 answer에 저장
            answer.append((totalTime,idx,music))

    if answer:
        answer = sorted(answer, key=lambda x: (-x[0], x[1])) # 재생시간에 대해 내림차순, 음악 순서인 idx에 대해서는 오름차순으로 정렬
        return answer[0][2]
    else:
        return '(None)'

print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]),"HELLO")
print(solution(	"CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]),"FOO")
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]),"WORLD")