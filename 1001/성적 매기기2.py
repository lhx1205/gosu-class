T = int(input())
grades = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    totals = [] # 총점 담을 리스트
    ratio = N//10
    for _ in range(N):
        mid, final, hw = map(int, input().split())
        totals.append(mid * 35 + final * 45 + hw * 20) # 중간 기말 과제 비율만큼 totals 리스트에 넣기

    k_score = totals[K - 1]          # 정렬 전에 K번 학생 점수를 변수로 지정해두기 (안그러면 정렬할 때 K번 학생의 위치가 꼬여버림)
    totals.sort(reverse=True)        # 총점 높은 순으로 정렬
    rank = totals.index(k_score)     # k번째 학생의 등수

    print(f'#{tc} {grades[rank // ratio]}')
    # 등수를 비율로 나눈 몫 ex) 20명일 때 2명씩 나뉘니까 0번, 1번 //2 하면 둘 다 0이므로 0번째인 A+,
    # 2,3 //2 하면 둘 다 1이므로 1번째인 A0 이런 방식.