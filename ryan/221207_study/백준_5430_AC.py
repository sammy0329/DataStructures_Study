"""
4
RDD
4
[1,2,3,4]
DD
1
[42]
RRD
6
[1,1,2,3,5,8]
D
0
[]
"""
import sys
from collections import deque

for _ in range(int(input())):
    command = sys.stdin.readline().strip()
    arr_len = int(sys.stdin.readline().strip())
    arr_ = list(sys.stdin.readline().strip('\n[]').split(','))
    if arr_len == 0:
        arr_ = []

    deq = deque(arr_)
    reverse = False

    answer = ''

    try:
        for each in command:
            if each == 'R':
                reverse = not reverse

            elif each == 'D':
                if reverse:
                    deq.pop()

                else:
                    deq.popleft()

    except IndexError:
        print('error')
        continue

    if reverse:
        deq.reverse()

    print('[', end='')
    for idx, each in enumerate(deq):
        print(each, end='')
        if idx != len(deq)-1:
            print(',', end='')

    print(']')
