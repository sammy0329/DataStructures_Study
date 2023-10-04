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
import copy


def visit(path, directed, num_tickets, results=[]):
    if len(path) == num_tickets+1:
        results.append(path)
        return results

    now = path[-1]

    for next_step in directed[now]:
        directed_ = copy.deepcopy(directed)
        directed_[now].remove(next_step)

        path_ = path + [next_step]

        visit(path_, directed_, num_tickets, results)

    return results


def solution(tickets):
    directed = {}

    for dep, dest in tickets:
        if directed.get(dep) is None:
            directed[dep] = [dest]
        else:
            directed[dep].append(dest)

    a = visit(['ICN'], directed, len(tickets))
    a.sort()
    # print(a[0])

    return a[0]


# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])