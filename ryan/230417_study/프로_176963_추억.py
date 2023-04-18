"""
name : 등장 이름
yearing : 등장 이름 별 점수

len(name), len(yearing) = [3, 100]

photo : 사진 별 name 리스트로 이뤄진 2D List

len(photo) = [1, 100]
"""


def solution(name, yearing, photo):

    answer = []

    info = {name_each:yearing[idx] for idx, name_each in enumerate(name)}

    for names in photo:
        score = 0

        for name_ in names:
            if info.get(name_) is not None:
                score += info[name_]

        answer.append(score)

    return answer


name, yearing, photo = ["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print(solution(name, yearing, photo))
# [19, 15, 6]

name, yearing, photo = ["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]
print(solution(name, yearing, photo))
# [67, 0, 55]

name, yearing, photo = ["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]]
print(solution(name, yearing, photo))
# [5, 15, 0]
