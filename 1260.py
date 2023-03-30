def bfs(v):
    from collections import deque
    q = deque([v])
    visit[v] = 1
    while q:
        v = q.popleft()
        print(v,end=' ')
        for i in range(1,n+1):
            if visit[i] == 0 and graph[v][i] == 1:
                q.append(i)
                visit[i] = 1


def dfs(v):
    visit2[v] = 1, print(v, end=' ')
    for i in range(1, n+1):
        if visit2[i] == 0 and graph[v][i] == 1:
            dfs(i)


n, m, v = map(int,input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a][b],graph[b][a] = 1, 1
visit = [0] * (n+1)
visit2 = [0] * (n+1)

dfs(v),print()
bfs(v)