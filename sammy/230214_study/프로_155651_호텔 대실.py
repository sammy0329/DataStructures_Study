def solution(book_time):
    # 시간을 총 분으로 변경하고 청소 시간 고려하여 (start,end+10)로 리스트에 저장
    new_book_times = [(int(s[:2]) * 60 + int(s[3:]), int(e[:2]) * 60 + int(e[3:])+10) for s, e in book_time]
    new_book_times.sort()

    rooms = []
    
    for new_book_time in new_book_times:
        if not rooms:
            rooms.append(new_book_time)
            continue

        for idx, room in enumerate(rooms):         
            if new_book_time[0] >= room[-1]:
                rooms[idx] = room + new_book_time
                break
        # for-else문을 통해 for문 중간에 break 되지 않고 끝까지 실행되었을 때 사용
        else:
            rooms.append(new_book_time)
            
    return len(rooms)

print(solution([["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]))
print(solution([["09:10", "10:10"], ["10:20", "12:20"]]))
print(solution([["10:20", "12:30"], ["10:20", "12:30"], ["10:20", "12:30"]]))