array = [1, 8, 7, 4, 3, 5, 6]
n = len(array)
prefix_sum = [0] * n

for i in range(n):
    for j in range(i+1):
        prefix_sum[i] += array[j]

print(prefix_sum)