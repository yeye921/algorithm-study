# ������ ������� ��ġ�ϴ� ��ȣ�� ������ �����ɷ� ����!
# ��ġ��ȣ ī���� & 0���� ī�����ϴ� ����̿�

def solution(lottos, win_nums):
    zero, cnt = 0,0 
    
    for i in range(6):
        if lottos[i] == 0:
            zero += 1       # �� �� ���� ��ȣ(0)�� ����
        else:
            if lottos[i] in win_nums: 
                cnt += 1
    
    arr = [cnt+zero,cnt]    # [�ְ����,��������]

    for i in range(2):
        if arr[i] == 6:
            arr[i] = 1
        elif arr[i] == 5:
            arr[i] = 2
        elif arr[i] == 4:
            arr[i] = 3
        elif arr[i] == 3:
            arr[i] = 4
        elif arr[i] == 2:
            arr[i] = 5
        elif arr[i] <= 1:
            arr[i] = 6
            
    return arr


# �� ���� Ǯ��
def solution(lottos,win_nums):
    rank = [6,6,5,4,3,2,1] # rank�� ����Ʈ�� ����� ����Ʈ!
    
    cnt = 0
    cntz = lottos.count(0) # 0�� ���� ī����
    
    for i in lottos:
        if i in win_nums:
            cnt += 1
            
    return rank[cnt+cntz],rank[cnt] # rank ����Ʈ�� ���ᰳ���� �ε����� �־� [�ְ����,��������]�� ����




# �ٸ� Ǯ��
def solution(lottos,win_nums):
    rank = {
        0:6,
        1:6,
        2:5,
        3:4,
        4:3,
        5:2,
        6:1
        }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]
