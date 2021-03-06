# https://www.acmicpc.net/problem/2747
# 피보나치 수
# 시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
# 1 초 (추가 시간 없음)	128 MB	31983	14450	11866	47.247%
# 문제
# 피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.

# 이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n>=2)가 된다.

# n=17일때 까지 피보나치 수를 써보면 다음과 같다.

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597

# n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 n이 주어진다. n은 45보다 작거나 같은 자연수이다.

# 출력
# 첫째 줄에 n번째 피보나치 수를 출력한다.

# 예제 입력 1 
# 10
# 예제 출력 1 
# 55

# 재귀 문제풀이
def solution(N):
    if N == 0:
        return 0
    if N == 1:
        return 1

    return solution(N-1) + solution(N-2)

print(solution(10))
# 55 

# 시간복잡도 2의 n승
# 피보나치수열 : 재귀적 구현의 한계
# 그래프로 표현했을 때, 중복되는 f(0),f(1)등 중복계산이 많아진다 
# 그래서 동적계획법으로 품



# 동적 계획법 풀이

def solution(N):
    a, b = 0, 1
    while N > 0:
        a, b = b, a + b
        N -= 1
    return a
# 0 1 1 2 3
# a b 
#   a b
#     a b
#       a b

print(solution(10))
# 55