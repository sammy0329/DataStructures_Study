import sys
from linked_list import Node, LinkedList

input_string = input()

ll = LinkedList()
buf = ll.root

for word in input_string:
    new_buf = Node(word, buf, None)
    buf.back = new_buf
    buf = new_buf

num_commands = int(input())

for _ in range(num_commands):
    command = sys.stdin.readline().strip().split()
    if command == 'L':
        buf = ll.get_front(buf)

    elif command == 'D':
        buf = ll.get_back(buf)

    elif command == 'B':
        buf = ll.self_destruction(buf)

    else:
        input_word = command.split()[-1]
        buf = ll.insert(buf, input_word)

    # # DEBUG PHASE
    # print('===============debug=================')
    # if buf.front is not None:
    #     print(f'front:{buf.front.value}')
    # else:
    #     print(f'front:None!!!!!')
    # print(f'value:{buf.value}')
    # if buf.back is not None:
    #     print(f'back:{buf.back.value}')
    # else:
    #     print(f'back:None!!!!!')

buf = ll.root
while buf.back is not None:
    buf = buf.back
    print(buf.value, end='')