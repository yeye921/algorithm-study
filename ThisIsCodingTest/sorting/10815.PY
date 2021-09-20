# 숫자카드 문제

import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

dict1 = {m_list[i]: 0 for i in range(len(m_list))}

for i in range(n):
    if n_list[i] in dict1.keys():
        dict1[n_list[i]] += 1
print(" ".join(map(str, list(dict1.values()))))