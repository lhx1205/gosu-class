T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    answer = 0

    for i in range(N-M+1):
        for j in range(N-M+1): # N x N의 행과 열
            fly = 0
            for ni in range(M):
                for nj in range(M): # M x M의 행과 열
                    fly += arr[i+ni][j+nj] # 각각 돌면서 MxM 칸 내부에 있는 파리 수 더해주기
            answer = max(fly, answer) # 각 칸 돌다가 이전 최댓값보다 현재 값이 더 크면 최댓값 갱신
            
    print(f'#{tc} {answer}')

