#처음풀이

# def solution(numbers):
#     answer = []
#     stack=[]
#     data=numbers.pop()
#     stack.append(data)
#     answer.append(-1)

#     while numbers:
#         data=numbers.pop()
#         stack.append(data)
#         for check_idx in range(len(stack)-1,-1,-1):
#             if data<stack[check_idx]:
#                 answer.append(stack[check_idx])
#                 break
#         else:
#             answer.append(-1)

#     return answer[::-1]

# stack 개념 활용.
def solution(numbers):
    answer = [-1]*len(numbers)
    stack=[]

    for idx in range(len(numbers)):
        
        while stack and numbers[stack[-1]]<numbers[idx]:
            answer[stack.pop()]=numbers[idx]
        stack.append(idx)

    return answer

print(solution([2, 3, 3, 5]),[3, 5, 5, -1])
print(solution([9, 1, 5, 3, 6, 2]),[-1, 5, 6, 6, -1, -1])
