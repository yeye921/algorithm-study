# �� �迭�� ���� �ƴ� ���� ����, remove()�̿�
def solution(arr):
    if len(arr)<=1:
        # �� �迭�� ���
        return [-1]
    else:
        # �ƴ� ���
        arr.remove(min(arr))
        return arr

# ����ȭ �ڵ�
def solution(arr):
    return [i for i in arr if i > min(arr)]
