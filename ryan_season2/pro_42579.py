"""
베스트 앨범

["classic", "pop", "classic", "classic", "pop"]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
"""
from collections import defaultdict


def solution(genres, plays):
    answer = []
    info = defaultdict(list)
    genre_play_sum = defaultdict(int)

    for idx, (genre, play) in enumerate(zip(genres, plays)):
        info[genre].append((play, idx))
        genre_play_sum[genre] += play

    genre_keys = list(genre_play_sum.keys())
    genre_keys.sort(key=lambda x: -genre_play_sum[x])

    for genre in genre_keys:
        if len(info[genre]) == 1:
            answer.append(info[genre][0][1])

        else:
            info[genre].sort(key=lambda x: (-x[0], x[1]))

            answer.append(info[genre][0][1])
            answer.append(info[genre][1][1])

    return answer


print(solution(["tred", "classic", "pop", "classic", "classic", "pop", "pop", "pop"], [15, 500, 600, 150, 800, 2500, 4000, 4000]))
