T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split()))for _ in range(N)]

    answer = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            fly = 0
            for ni in range(i,i+M):
                for nj in range(j,j+M):
                    fly += arr[ni][nj]
            answer = max(fly, answer)
            
    print(f'#{tc} {answer}')