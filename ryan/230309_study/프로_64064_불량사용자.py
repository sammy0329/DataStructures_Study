def is_possible(origin_word: str, masked_word: str):
    if len(origin_word) != len(masked_word): return False

    for idx, spell in enumerate(masked_word):
        if spell == '*': continue
        if spell != origin_word[idx]: return False

    else: return True


def solution(user_id, banned_id):
    from itertools import permutations

    iter_ = permutations(user_id, len(banned_id))

    candidate = []
    for sample in iter_:
        for idx in range(len(banned_id)):
            if not is_possible(sample[idx], banned_id[idx]):
                break

        else:
            if not set(sample) in candidate:
                candidate.append(set(sample))

    return len(candidate)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

print(solution(user_id, banned_id))
