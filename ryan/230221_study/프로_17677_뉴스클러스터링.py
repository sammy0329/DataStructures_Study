def split2(words) -> list:
    words = words.lower()

    result = []

    for idx in range(len(words) - 1):
        front, back = words[idx], words[idx + 1]
        if 97 <= ord(front) <= 122 and 97 <= ord(back) <= 122:
            result.append(front + back)

    return result


def solution(str1, str2):
    # 1. 소문자로 만든 뒤
    # 2. ascii코드 기반 특문 필터링 해 2글자쌍 리턴 (list)
    # 3. 2개의 리턴으로 자카드 유사도 산출
    split_set1 = split2(str1)
    split_set2 = split2(str2)

    all_set = set(split_set1 + split_set2)

    union_count = 0
    intersection_count = 0

    for each in all_set:
        freq_1 = split_set1.count(each)
        freq_2 = split_set2.count(each)

        union_count += max(freq_1, freq_2)
        intersection_count += min(freq_1, freq_2)

    if union_count == 0: return 65536

    return int(intersection_count / union_count * 65536)