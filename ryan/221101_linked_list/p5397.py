import sys
from linked_list import LinkedList

num_commands = int(input())

for _ in range(num_commands):
    input_string = sys.stdin.readline().strip()

    ll = LinkedList()
    buf = ll.root

    for word in input_string:
        if word == '<':
            buf = ll.get_front(buf)

        elif word == '>':
            buf = ll.get_back(buf)

        elif word == '-':
            buf = ll.self_destruction(buf)

        else:
            buf = ll.insert(buf, word)

    buf = ll.root
    while buf.back is not None:
        buf = buf.back
        print(buf.value, end='')
    print()
