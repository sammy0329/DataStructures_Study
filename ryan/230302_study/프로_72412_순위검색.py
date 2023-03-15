"""
language [cpp, java, python]
position [frontend, backend]
car [junior, senior]
food [chicken, pizza]

info [1, 50000] 지원자 수, language, position, car ,food, score
query [1, 100000] 쿼리 수 language and postiion and car and soulfood

bucket = {
    'language': {'cpp': [], 'java': [],: 'python': []},
    'position': {'frontend': [], 'backend': []},
    'car': {'junior': [], 'senior': []},
    'food': {'chicken': [], 'pizza': []}
}
"""


def binary_search(target, min_score):
    lo = 0
    hi = len(target)-1

    while lo <= hi:
        mid = (lo + hi) // 2

        if target[mid] >= min_score:
            hi = mid - 1
        elif target[mid] < min_score:
            lo = mid + 1

    return lo


def solution(info, query):
    answer = []
    scores = {}
    bucket = {'language': {'cpp': [], 'java': [],'python': []},
              'position': {'frontend': [], 'backend': []},
              'career': {'junior': [], 'senior': []},
              'soul': {'chicken': [], 'pizza': []},
              'score': {}
              }

    for idx, line in enumerate(info):
        language, posision, career, soul, score = line.split()

        bucket['language'][language].append(idx)
        bucket['position'][posision].append(idx)
        bucket['career'][career].append(idx)
        bucket['soul'][soul].append(idx)
        scores[idx] = int(score)

    target_cache = {}
    for each in query:
        parse = each.split()
        language_ = parse[0]
        position_ = parse[2]
        career_ = parse[4]
        soul_ = parse[6]
        score = int(parse[7])

        target_type = language_[0] + position_[0] + career_[0] + soul_[0]

        if target_cache.get(target_type) is None:
            target = set([i for i in range(len(info))])
            if language_ != '-': target = set(bucket['language'][language_])
            if position_ != '-': target = set(bucket['position'][position_]) & target
            if career_ != '-': target = set(bucket['career'][career_]) & target
            if soul_ != '-': target = set(bucket['soul'][soul_]) & target

            temp = [scores[idx] for idx in target]
            temp.sort()

            target_cache[target_type] = temp

        else:
            temp = target_cache[target_type]

        ans = len(temp) - binary_search(temp, score)
        answer.append(ans)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

# result = [1,1,1,1,2,4]

print(solution(info, query))
