T = int(input())


def circle():
  for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 1, 0, 0]  # 상, 하, 좌, 우
    dy = [0, 0, -1, +1]

    max_count = 0

    for i in range(N):
      for j in range(N):
        cur_i, cur_j = i, j
        cnt = 1  # count 대신 cnt 사용 (함수 충돌 방지)

        while True:
          next_i, next_j = -1, -1
          min_val = float('inf')

          for k in range(4):
            ni = cur_i + dx[k]
            nj = cur_j + dy[k]

            if 0 <= ni < N and 0 <= nj < N:
              if arr[ni][nj] < arr[cur_i][cur_j]:
                if arr[ni][nj] < min_val:
                  min_val = arr[ni][nj]
                  next_i, next_j = ni, nj

          if next_i != -1:
            cur_i, cur_j = next_i, next_j
            cnt += 1
          else:
            break

        max_count = max(max_count, cnt)

    print(f'#{tc} {max_count}')


circle()