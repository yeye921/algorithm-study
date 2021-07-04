# ������ �������� -> %������ �̿�, ������ ������ ���, ���ο� �迭�� ���� �� ����
def solution(arr, divisor):
    result = []
    for i in arr:
        if i % divisor == 0:
            result.append(i)
    if len(result)==0:
        result.append(-1)
    else:
        result.sort()
    return result


# �ٸ� Ǯ�� - ����Ʈ �������ڼ� �̿�
def solution(arr, divisor):
    result = [i for i in arr if i%divisor==0]
    if len(result) ==0:
        result.append(-1)
    else:
        result.sort()
    return result


# �ٸ� Ǯ�� 2
def solution(arr, divisor):
    result = [i for i in arr if i%divisor==0]
    if len(result) ==0:
        return [-1]
    else:
        return sorted(result)  # result.sort()�� ��� null�� ��ȯ!

# ����ȭ �ڵ�(or �̿�)
# ����Ʈ�� ���� ������ True�̰� ������ False�� ���� �̿�
def solution(arr,divisor):
    return sorted([i for i in arr if n%divisor == 0]) or [-1]




