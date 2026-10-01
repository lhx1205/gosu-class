T = int(input())


def circle(): # 함수 정의
  for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dy = [0, 0, -1, +1]

    max_count = 0 # 최대 몇 칸?

    for i in range(N): 
      for j in range(N):
        cur_i, cur_j = i, j #i랑 j를 시작점으로 설정하기
        cnt = 1 # 시작칸 포함해서 1로 시작

        while True:
          next_i, next_j = -1, -1 # 좌표가 0부터 시작하니까,, 이동할 수 있는 다음 칸 찾았는지 판별 (이게 헷갈림)
          min_val = float('inf') # 가장 작은 값을 찾으려고 엄청 작은 값으로 초기값 설정하기

          for k in range(4):
            ni = cur_i + dx[k] # 상 하 좌 우 돌면서 현재 위치에서 이동하는데
            nj = cur_j + dy[k]

            if 0 <= ni < N and 0 <= nj < N: # 범위에서 벗어나지 않으면
              if arr[ni][nj] < arr[cur_i][cur_j]: # 다음에 갈 칸의 숫자가 더 작아야 함 
                if arr[ni][nj] < min_val: # 이동할 칸이 최솟값보다 작으면
                  min_val = arr[ni][nj]
                  next_i, next_j = ni, nj # 계속 작은 값을 갱신

          if next_i != -1: # -1의 의미가 이동할 곳을 못 찾았다는 것, -1이 아니면 이동할 수 있는 칸을 찾았다는 뜻
            cur_i, cur_j = next_i, next_j # 현재 위치를 더 작은 이동할 칸으로 바꿈
            cnt += 1 # 이동했으니까 cnt +=1
          else:
            break #아니면 break

        max_count = max(max_count, cnt) # 이동 횟수의 최댓값 찾기

    print(f'#{tc} {max_count}')


circle()
