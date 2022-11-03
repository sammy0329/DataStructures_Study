T=int(input())

for _ in range(T):
    strings=[]
    data=list(input())

    cursor=0
    for j in data:
        if j=='<':
            if cursor>0 and len(strings)>0:
                cursor-=1
                # print(strings,cursor)
        elif j=='>':
            if cursor<len(strings) and len(strings)>0:
                cursor+=1
                # print(strings,cursor)
        elif j=='-':
            if cursor>0 and len(strings)>0:
                cursor-=1
                strings.pop(cursor)
                
                # print(strings,cursor)
        else:
            #strings.insert(cursor, j) -> o(n)
            after=strings[cursor:]
            strings=strings[:cursor]
            strings.append(j)
            strings.extend(after)

            cursor+=1
            # print(strings,cursor)
    for i in strings:
        print(i,end='')
    print()
