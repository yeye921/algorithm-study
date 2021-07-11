# 매번 가장 작은 것을 선택하는 알고리즘 
# 가장 작은 데이터를 앞으로 보내는 과정을 N-1번 반복하면 정렬이 완료됨


def selection_sort(arr):
    for i in range(len(arr)):
        min = i   # 가장 작은 원소의 인덱스 
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j

        arr[i],arr[min] = arr[min],arr[i]


array = [7,5,9,0,3,1,6,2,4,8]
selection_sort(array)
print(array)
  
