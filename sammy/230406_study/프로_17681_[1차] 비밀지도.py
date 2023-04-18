def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        # 2진법으로 변환
        arr1_bin=bin(arr1[i])[2:]
        arr2_bin=bin(arr2[i])[2:]

        # 앞에 0을 붙여준다.
        arr1_bin=arr1_bin.zfill(n)
        arr2_bin=arr2_bin.zfill(n)

        answer_bin=''

        for j in range(n):
            if arr1_bin[j]=='1' or arr2_bin[j]=='1':
                answer_bin+='#'
            else:
                answer_bin+=' '
        answer.append(answer_bin)
  
    return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]),["#####", "# # #", "### #", "#  ##", "#####"])
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]),["######", "###  #", "##  ##", " #### ", " #####", "### # "])
