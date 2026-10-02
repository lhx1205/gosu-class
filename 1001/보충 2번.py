# N명의 사람이 수직선 위에 있고, i번째 사람은 x에 서서 G또는 H팻말을 들고 있음
# 수직선 위에 임의의 구간을 찍고 사진의 크기는 K
# 사진을 찍었을 때, G는 1점 H는 2점으로 계산해서 사진 한 번에 가장 많은 점수를 얻는 프로그램
# =====================================================================================

# 풀이 1번
# n, k = map(int, input().split())
# line = [0] * 10002

# for _ in range(n):
#     pos, char = input().split() # 각 사람의 위치와 팻말 종류 입력
#     line[int(pos)] = 1 if char == 'G' else 2 # int(pos)값에 대하여 char가 G면 1 아니면 2

# answer = -1 # 최댓값 구할거니까 0이하로 설정

# for s in range(1, 10002): # i+k가  범위를 벗어나지 않는 최대치만큼 거리 설정
#     if s + k > 10001: # 현재 위치에서 k만큼 갔을 때 범위를 벗어나면
#         continue # 다음으로 넘어가기
# # answer값과 수직선 위에 s에서 s+k+1 범위(최대 거리까지 구할건데 인덱스니까 +1)까지 더한 값의 최댓값
#     answer = max(answer, sum(line[s:s+k+1])) 

# print(answer)
#======================================================================================

#풀이 2번

n, k = map(int, input().split())
people = []
for _ in range(n):
    pos, char = input().split()

    score = 1 if char == 'G' else 2

    people.append((int(pos), score))

answer = -1
for i in range(n):
    start = people[i][0] # 시작 위치, [0]은 위치를 의미

    current_score = 0
    for j in range(n):
        target_pos = people[j][0]
        if start <= target_pos <= start + k:
            current_score += people[j][1] # [1]은 점수를 의미

    answer = max(answer, current_score)

print(answer)