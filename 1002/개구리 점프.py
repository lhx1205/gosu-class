# 길이 N인 웅덩이, 점프 거리 K
# 나뭇잎이 있으면 1 없으면 0
# 가장 왼쪽에서 점프 시작하고(인덱스 0번부터)

# 경우 다 나눠보기
# 1. 끝까지 점프 다 했을 때, 또는 최대 범위를 넘어갔을 때 => 최대 이동 거리 == N
# 2. 중간에 끊기는 경우
# -- 1. 시작점에서 뛰었는데 나뭇잎이 K안에 존재하지 않을 때 => 최대 이동 거리 == 떨어진 지점
# 3. 점프 계속 진행하는데 사이에 1이 있으면 start를 그 지점으로 갱신
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    start = 0  # 시작점
    answer = 0 # 점프 뛴 최대 거리

    while True:
        # 점프했는데 웅덩이를 넘어가거나 도달하면 종료
        if start + K >= N:
            answer = N
            break

        # start + K 부터 start + 1까지 역순으로 나뭇잎(1) 찾기 (시작점과 K 사이에 있는 나뭇잎 찾기)
        for i in range(start + K, start, -1):
            if arr[i] == 1:
                start = i  # 나뭇잎을 찾으면 시작점을 그 위치로 갱신
                break
        else:
            # for 문이 break 되지 않고 끝까지 돌았다면
            # -> K칸 이내에 나뭇잎이 하나도 없었다
            answer = start + 1 + K
            break

    print(f'#{tc} {answer}')