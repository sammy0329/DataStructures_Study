"""
단속 카메라

차량의 대수는 1대 이상 10,000대 이하입니다.
routes에는 차량의 이동 경로가 포함되어 있으며 routes[i][0]에는 i번째 차량이 고속도로에 진입한 지점, routes[i][1]에는 i번째 차량이 고속도로에서 나간 지점이 적혀 있습니다.
차량의 진입/진출 지점에 카메라가 설치되어 있어도 카메라를 만난것으로 간주합니다.
차량의 진입 지점, 진출 지점은 -30,000 이상 30,000 이하입니다.

routes	return
[[-20,-15], [-14,-5], [-18,-13], [-5,-3]]	2
"""
# CHECK


def solution(routes):
    answer = 1

    s = -30000
    e = 30000

    routes.sort(key=lambda x:(x[0], -x[1]))
    for sp, ep in routes:
        if s <= sp <= e or s <= ep <= e:
            s = max(s, sp)
            e = min(e, ep)

        else:
            s = sp
            e = ep

            answer += 1

    return answer


print(solution([[-20, -15], [-14, -5], [-18, -13], [-5, -3]]))
