import re


def hnt_split(file_name: str):
    pattern = '[0-9]{1,5}'
    search_NUMBER = re.search(pattern, file_name)

    span = search_NUMBER.span()
    start = span[0]
    end = span[1]

    HEAD_ = file_name[:start]
    NUMBER_ = file_name[start:end]
    TAIL_ = file_name[end:]

    return HEAD_, NUMBER_, TAIL_


def solution(file_list):

    file_info = {}
    sorted_result = []

    for file_ in file_list:
        head_, number_, tail_ = hnt_split(file_)

        head_ = head_.lower()
        number_ = int(number_)

        if file_info.get(head_) is None:
            file_info[head_] = {number_: [file_]}

        else:
            if file_info[head_].get(number_) is None:
                file_info[head_][number_] = [file_]

            else:
                file_info[head_][number_].append(file_)

    for sorted_head in sorted(file_info.keys()):
        for sorted_tail in sorted(file_info[sorted_head].keys()):
            buffer = file_info[sorted_head][sorted_tail]

            sorted_result += buffer

    return sorted_result


print(solution(["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]))

