import sys
import heapq


class Question:
    def __init__(self):
        self.pre_count = 0
        self.child = []


num_question, pre_info = map(int, input().split())

question_list = [Question() for _ in range(num_question)]
is_inque = [False for _ in range(num_question)]
heapque = []
count = 0

for _ in range(pre_info):
    before, after = map(int, sys.stdin.readline().strip().split())
    before, after = before-1, after-1

    question_list[after].pre_count += 1
    question_list[before].child.append(after)

while count < num_question:
    for idx, q in enumerate(question_list):
        if is_inque[idx]:
            continue

        if q.pre_count == 0:
            heapq.heappush(heapque, idx)
            is_inque[idx] = True

            break

    now_visit = heapq.heappop(heapque)
    for each_child in question_list[now_visit].child:
        question_list[each_child].pre_count -= 1
    print(now_visit+1, end=' ')
    count += 1
