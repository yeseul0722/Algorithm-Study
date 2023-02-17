import sys
sys.stdin = open('input2.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    mat = []
    for _ in range(N):
        data = list(map(int, input().split()))
        mat.append(data)
    for i in range(N):
        for j in range(M):
            print(mat[i][j])