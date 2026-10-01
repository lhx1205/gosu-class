# 정수 N개로 이루어진 수열 A1~ An 까지 주어짐
# 수열에서 연속한 k개의 원소, 즉 어떤 i에 대해 Ai~~를 골랐을 때 K개 원소의 합이 최대가 되는 프로그램

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.


# max_val = 0
# for i in range(n-k+1):
#     ans = 0
#     for j in range(i,i+k):
#         ans+=arr[j]

#     if ans > max_val:
#         max_val = ans

# print(max_val)

answer = -1
for i in range(n-k+1):
    answer = max(answer, sum(arr[i:i+k]))

print(answer)