# 정렬할 배열의 요소를 그룹으로 나눠 각 그룹 별로 삽입 정렬을 수행하고, 
# 그 그룹을 합치면서 정렬을 반복하여 요소의 이동 횟수를 줄이는 방법 

def shell_sort(arr):
    N = len(arr)
    h = N // 2
    while h > 0:
        for i in range(h, N):
            temp = arr[i]
            j = i - h
            while j >= 0 and arr[j] > temp:
                arr[j + h] = arr[j]
                j -= h
            arr[j + h] = temp
        h //= 2
 
    print(arr)
 
 
arr = [8, 1, 4, 2, 7, 6, 3, 5]
shell_sort(arr)

