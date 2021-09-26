# 특정 거리의 도시 찾기 문제

import sys
input = sys.stdin.readline
from collections import deque

n,m,k,x = map(int,input().split()) #도시 개수, 도로 개수, 거리 정보, 출발 도시 번호
#x에서 출발하여 거리가 k인 모든 도시를 찾아야 한다 
graph = [[] for _ in range(n+1)]
answer = [-1] * (n+1)
answer[x] = 0 

for _ in range(m):
    a, b = list(map(int,input().split()))
    graph[a].append(b)
que = deque([x])

while que:
    now = que.popleft()
    for nxt in graph[now]:
        if answer[nxt] == -1:
            answer[nxt] = answer[now] + 1 
            que.append(nxt) 

for i in range(n+1):
    if answer[i] == k:
        print(i)

if k not in answer:
    print(-1)