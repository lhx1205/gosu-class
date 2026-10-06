# 연속으로 커지면 개수 +
# 최소 길이는 1로 두고 시작
# 커질때마다 cnt +=1 하고, cnt가 최댓값을 넘어가면 갱신

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 당근 개수
    arr = list(map(int, input().split())) # 당근의 크기가 적힌 리스트

    max_val = 1 # 최댓값 (커지지 않는 경우 1이므로 1부터 시작)
    cnt = 1  # 커진 횟수, 연속으로 커지지 않으면 최소 길이 1
    for i in range(N-1): # i+1이 범위 벗어나는걸 방지, N-1로 두고 돌기
        if arr[i] < arr[i+1]: # 커질 때
            cnt += 1 # 횟수 +1

        else:
            cnt = 1

        if cnt > max_val:
            max_val = cnt

    print(f'#{tc} {max_val}')