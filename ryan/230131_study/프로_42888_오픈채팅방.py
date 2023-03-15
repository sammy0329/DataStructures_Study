def solution(record):
    info = {}
    output = []
    parse = [line.split() for line in record]

    for log in parse:
        if log[0] == 'Leave': continue

        event, uid, info[uid] = log

    for log in parse:
        event, uid = log[0:2]
        if event == 'Enter': output.append(f'{info[uid]}님이 들어왔습니다.')
        elif event == 'Leave': output.append(f'{info[uid]}님이 나갔습니다.')

    return output
