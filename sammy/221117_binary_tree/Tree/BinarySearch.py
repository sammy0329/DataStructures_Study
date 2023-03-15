def binary_search(array,target,start,end):
    if start>end:
        return None
    
    mid=(start+end)//2
    
    if array[mid]==target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인하기
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
	# 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array,target,mid+1,end)

# n개 원소의 개수와 찾고 싶은 target 입력받기
n,target=map(int,input().split())

array=list(map(int,input().split()))

result=binary_search(array,target,0,n-1)