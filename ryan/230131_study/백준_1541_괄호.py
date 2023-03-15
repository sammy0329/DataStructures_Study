def strCalculater(equation:str):
    return sum(map(int, equation.split('+')))


sumValue = 0
equation = input().split('-')

for idx, each in enumerate(equation):
    if idx == 0:
        if each != '':
            sumValue += strCalculater(each)
            continue
    else:
        sumValue -= strCalculater(each)

print(sumValue)
