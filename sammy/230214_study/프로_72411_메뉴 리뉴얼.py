from itertools import combinations

def solution(orders, courses):
    answer = []
    
    for course in courses:
        menus = dict()
        combi_list = list()
        
        # orders를 course 개수의 조합을 구하기
        for order in orders:
            # "WXA"처럼 뒤죽박죽 섞여 있으므로 순서대로 정렬해서 조합진행
            combi_list.extend(list(combinations(sorted(order), course))) 
        
        for combi in combi_list:
            data = ''.join(combi)
            # 딕셔너리에 있으면 +1 없으면 1로 처리
            if data in menus:
                menus[data] += 1
            else:
                menus[data] = 1
        
        for menu in menus:
            if max(menus.values()) > 1: # 딕셔너리 value 값의 max 값이 1보다 클 때
                if menus[menu] == max(menus.values()): # max 값과 일치하는 값들 answer에 append
                    answer.append(menu)
                    
    answer.sort() # 오름차순으로 정렬

    return answer

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]),["AC", "ACDE", "BCFG", "CDE"])
# print(solution(	["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]),	["ACD", "AD", "ADE", "CD", "XYZ"])
# print(solution(["XYZ", "XWY", "WXA"],[2,3,4]),["WX", "XY"])