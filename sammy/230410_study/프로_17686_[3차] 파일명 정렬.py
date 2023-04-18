import re

def solution(files):
    answer = []
    # re를 통해 숫자로 split 진행하여 answer에 append 
    for file in files:
        split_file=re.split(r'([0-9]+)',file)
        print(split_file)
        answer.append(split_file)
    
    # 모두 소문자로 변경 후 sort 진행 후, 숫자로 한번 더 sort 진행
    answer=sorted(answer,key=lambda x:(x[0].lower(), int(x[1])))
        
        

    return [''.join(check) for check in answer]

print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]),["img1.png", "IMG01.GIF", "img02.png", "img2.JPG", "img10.png", "img12.png"])
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]),["A-10 Thunderbolt II", "B-50 Superfortress", "F-5 Freedom Fighter", "F-14 Tomcat"])
