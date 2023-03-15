def solution(phone_book):
    hash_map = {}
    for each in phone_book:
        hash_map[each] = 1

    for each in phone_book:
        gets = ''
        for number in each:
            gets += number

            if hash_map.get(gets) is not None and gets != each:
                return False
    else:
        return True


if __name__ == '__main__':
    # inp = ["119", "97674223", "1195524421"]
    # inp = ["123", "456", "789"]
    inp = ["12", "123", "1235", "567", "88"]

    print(solution(inp))
