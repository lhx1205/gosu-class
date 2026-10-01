T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 1 # 숫자가 하나만 주어지는 경우에도 만족하기 때문에 1로 두고 시작하고,
    # cnt가 0이 되는 경우만 따지면 답을 구할 수 있다.
    for i in range(N-1): # i+1이 초과하는 경우를 방지하기 위해 N-1로
        if arr[i] <= arr[i+1]: # i번째의 값이 i+1의 값보다 작거나 같은 경우,
            cnt = 0 # 0으로 출력

    print(f'#{tc} {cnt}')