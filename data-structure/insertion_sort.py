# �����͸� �ϳ��� Ȯ���ϸ� �� �����͸� ������ ��ġ�� �����ϴ� �˰��� 
# �����Ͱ� ���� ���ĵǾ� ���� �� �ſ� ������ ����


def insertion_sort(arr):
    for i in range(1,len(arr)):
        for j in range(i,0,-1):  # i~1���� �����ϸ� �ݺ� 
            if arr[j] < arr[j-1]: # �� ĭ�� �������� �̵� 
                arr[j],arr[j-1] = arr[j-1], arr[j]
            else:        # �ڽź��� ���� �����͸� ������ �� ��ġ���� ���� 
                break


array = [7,5,9,0,3,1,6,2,4,8]
insertion_sort(array)
print(array)
