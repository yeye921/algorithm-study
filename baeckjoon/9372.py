# 상근이의 여행 문제

# 풀이-1
import sys

for t in range(int(input())):
    N, M = map(int, input().split())
    for i in range(M):
        a, b = map(int, sys.stdin.readline().split())

    print(N-1)

# 풀이-2
import sys

def dfs(node, cnt):
    check[node] = 1
    for n in graph[node]:
        if check[n] == 0:
            cnt = dfs(n, cnt+1)
    return cnt

for _ in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    check = [0]*(N+1)
    check[1] = 0
    cnt = dfs(1, 0)
    print(cnt)