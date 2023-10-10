"""
여행경로

모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

tickets	return
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	["ICN", "JFK", "HND", "IAD"]
[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
"""
from collections import defaultdict


def visit(path, directed, num_tickets, results=None):
    if results is not None:
        return results

    if len(path) == num_tickets+1:
        results = path

        return results

    now = path[-1]

    if sum(directed[now].values()) == 0:
        return results

    for next_step, cnt in sorted(directed[now].items()):
        if cnt == 0:
            continue

        directed[now][next_step] -= 1

        path_ = path + [next_step]

        results = visit(path_, directed, num_tickets, results)
        directed[now][next_step] += 1

    return results


def solution(tickets):
    directed = defaultdict(lambda: defaultdict(int))
    for dep, dest in tickets:
        directed[dep][dest] += 1

    answer = visit(['ICN'], directed, len(tickets))

    return answer


solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
solution([["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]])
