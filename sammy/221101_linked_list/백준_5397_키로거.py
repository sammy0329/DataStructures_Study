T=int(input())

for _ in range(T):
    left=[]
    right=[]
    data=list(input())
    # stack 응용

    for j in data:
        if j=='<':
            if left:
                right.append(left.pop())
        elif j=='>':
            if right:
                left.append(right.pop())

        elif j=='-':
            if left:
                left.pop()

        else:
            left.append(j)

    left.extend(reversed(right))


    for i in left:
        print(i,end='')
    print()
