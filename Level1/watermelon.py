# n�� Ȧ���� ���� ¦���� ���� ����
def solution(n):
    if n%2==0:
        return "����"*(n//2)  # ¦���� ��쵵 //������ ����ؾ� �����ȳ�, why?
    else:
        return "����"*(n//2)+"��"


# �ٸ� Ǯ��1
def solution(n):
    return "����"*(n//2) + "��"*(n%2) 

# �ٸ� Ǯ��2
def solution(n):
    s = "����" * n
    return s[:n]
