# �Ź� ���� ���� ���� �����ϴ� �˰��� 
# ���� ���� �����͸� ������ ������ ������ N-1�� �ݺ��ϸ� ������ �Ϸ��


def selection_sort(arr):
    for i in range(len(arr)):
        min = i   # ���� ���� ������ �ε��� 
        for j in range(i+1,len(arr)):
            if arr[min] > arr[j]:
                min = j

        arr[i],arr[min] = arr[min],arr[i]


array = [7,5,9,0,3,1,6,2,4,8]
selection_sort(array)
print(array)
  
