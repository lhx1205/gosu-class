# N명의 야구 선수, K의 실력 차이
# 팀원 +1 해가면서 실력 차이 비교하기
# 정렬해서 실력 가장 좋은 애를 기준 잡고
# (제일 잘하는 애 - 실력 차)와 같거나 더 수치가 높은 애만 팀원에 합류
# 인원이 최대가 되게 하기 위해 최댓값을 팀원이 늘어날 때마다 갱신해주기
T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort() # 오름차순 정렬해서 나타내기 편하게 함
    max_player = 0 # 팀 인원 최대치
    for i in range(N):
        player = arr[i] # 현재 기준으로 가장 높은 실력을 가진 사람
        team = 0 # 팀원 수
        for j in range(i+1):
            if arr[j] >= arr[i] - K: # 최댓값에서 실력차를 뺀 값보다 크거나 같으면 팀원에 합류
                team += 1

        if team > max_player: # 팀원 수가 이전 팀 인원 최댓값을 넘어가면
            max_player = team # 최댓값 갱신하기

    print(f'#{tc} {max_player}')