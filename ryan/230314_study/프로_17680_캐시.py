def solution(cacheSize: int, cities: list[str]) -> int:
    if cacheSize == 0: return len(cities) * 5

    from collections import deque

    total_time: int = 0
    cache: deque[str] = deque(['' for _ in range(cacheSize)])

    for query in cities:
        query = query.lower()

        if query in cache:
            cache.remove(query)
            cache.append(query)

            total_time += 1

        else:
            cache.popleft()
            cache.append(query)

            total_time += 5

    return total_time


print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))  # 21
print(solution(2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))  # 60
print(solution(5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]))  # 52
print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))  # 16
print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 25
