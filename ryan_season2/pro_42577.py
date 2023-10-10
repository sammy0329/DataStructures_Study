"""
전화번호 목록

phone_book	return
["119", "97674223", "1195524421"]	false
["123","456","789"]	true
["12","123","1235","567","88"]	false
"""
from collections import defaultdict


def solution(books):
    hash_books = defaultdict(int)

    books.sort(key=len)

    for each in books:
        parts = ''
        for word in each:
            parts += word
            if hash_books[parts] != 0:
                return False

        hash_books[each] = 1

    return True


print(solution(["119", "97674223", "1195524421"]))
print(solution(["123","456","789"]))
print(solution(["12","123","1235","567","88"]))
