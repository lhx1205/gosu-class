# 중간 35%, 기말 45%, 과제 20%
# 학생 수 N , 학점을 알고싶은 학생 번호가 K
# 평점은 N/10 으로 순서대로 부여함
# N/10.. 정수로 처리 ?
# 3xN의 2차원 리스트에 점수를 채워넣기
# K 학생의 총점 0.35 * arr[K][0]+ 0.45 * arr[K][1] + 0.2*arr[K][2]
T = int(input())

for tc in range(1, T + 1):
    # 학점 리스트
    score = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    total = []  # 학생 번호, 총점 담을 리스트
    N, K = map(int, input().split())  # N: 학생 수, K: 학점을 알고 싶은 학생 번호

    for i in range(N):
        arr = list(map(int, input().split()))

        # 총점 계산
        sum_val = 0.35 * arr[0] + 0.45 * arr[1] + 0.2 * arr[2]

        # 1번 학생부터 시작하기 위해 (i + 1)과 계산된 총점(sum_val)을 튜플로 묶어서 total 리스트에 추가하기
        total.append((i + 1, sum_val))

        # N명을 10개의 등급으로 나누기 위해, 한 등급당 들어갈 학생 수
    ratio = N // 10

    # 총점이 높은 순서대로(내림차순, reverse=True) 학생들 정렬합니다. (x[1]은 총점)
    sort_val = sorted(total, key=lambda x: x[1], reverse=True)

    # 정렬된 학생 목록을 순회하며 등급 부여 (a는 등급 인덱스 순번, b는 (학생 번호, 총점) 튜플)
    for a, b in enumerate(sort_val):
        # 학생 번호가 K이면,,
        if b[0] == K:
            # a(등수 순번)를 ratio(구간 크기)로 나눈 몫이 score 리스트의 인덱스
            # 예를 들어 score[0]은 A+,, 30명이라고 하면 3명씩 나눔, 0,1,2를 3으로 나눈 몫 ==> 0이니까 index[0]번인 A+이 됨.
            print(f"#{tc} {score[a // ratio]}")
            # K번 학생의 학점을 찾았으니 반복문 종료.
            break