T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    mat = []
    total = []
    for _ in range(N):
        data = list(map(int, input().split()))
        mat.append(data)
    for i in range(M):
        for j in range(M):

