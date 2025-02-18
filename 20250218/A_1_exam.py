# N 개의 화분에 비료를 주는데,
# 같은 비료를 연속해서 주면 P 만큼 덜 자란다.
# 1번 비료를 주면 line 1 만큼 각각 자라고, 2번 비료를 주면 line 2 만큼 각각 자란다.
# 식물이 자라는 높이의 합이 가장 큰 경우를 찾고, 그 높이를 모두 더해서 출력해라.

T = int(input())

N, P = map(int, input().split())

fertile1 = list(map(int, input().split()))
fertile2 = list(map(int, input().split()))

