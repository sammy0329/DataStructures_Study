def solution(book_time):
    every_minutes_of_day = [0 for _ in range(1440)]

    for start, end in book_time:
        start_hour, start_minute = map(int, start.split(':'))
        end_hour, end_minute = map(int, end.split(':'))

        start = (start_hour * 60) + start_minute
        end = (end_hour * 60) + end_minute
        end = min(end + 10, 1439)

        for each_minute in range(start, end):
            every_minutes_of_day[each_minute] += 1

    answer = max(every_minutes_of_day)

    return answer