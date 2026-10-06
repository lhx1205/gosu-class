T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split()) # 판넬의 크기, 렌즈의 크기
    matrix = [list(map(int, input().split()))for _ in range(N)] # 판넬의 에너지 정보
    arr = [list(map(int, input().split()))for _ in range(M)] # 렌즈의 에너지 정보
    # M을 N위에 계속 스캔하면서 (N-M+1)만큼 [i][j] 스캔
    # M의 전체 합은 계속 더하는데,, N은 각 칸의 수만큼 더하고
    print(f'#{tc}')
    for i in range(N-M+1): # 판넬 위에서 세로 방향 이동
        for j in range(N-M+1): # 판넬 위에서 가로 방향 이동
            eng = 0
            for mi in range(M): #렌즈 내부 탐색 (행)
                for mj in range(M): # 렌즈 내부 탐색(열)
                    eng += matrix[i+mi][j+mj] + arr[mi][mj] # 판넬 위치의 값 + 렌즈 위치의 값
            print(eng, end=" ")
        print() # 다음 줄로 넘어감 for mi mj 밖에 있어야됨