def solution(relation):
    from itertools import combinations

    column_length = len(relation[0])

    results = []

    for amount in range(1, column_length+1):
        candidates = combinations(range(column_length), amount)
        for candidate in candidates:

            for result in results:
                result: set
                if result.issubset(set(candidate)): break

            else:
                sample = []
                for row in relation:
                    rows = [row[col] for col in candidate]

                    if rows in sample: break
                    else: sample.append(rows)

                else:
                    results.append(set(candidate))

    return len(results)


relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))
