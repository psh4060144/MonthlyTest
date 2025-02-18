# N 명의 학생과, 그 학생들 중 두 명을 뽑아 키를 비교하는 행위를 M 번 반복한다.
# M 줄에 걸쳐 키를 비교한 결과가 a, b 형태로 나열되는데, a 학생이 b 학생보다 작다는 뜻이다.
# 자신의 키가 몇 번째인지 알 수 있는 학생이 모두 몇 명인가?

# idea
# 자신과 키를 비교한 친구를 모두 1로 표시. 자신도 1로 표시.
# 1을 따라갔을 때 위쪽, 오른쪽에 도달할 수 있다면 내가 얼마나 큰 지 알 수 있다.

T = int(input())

N = int(input())

M = int(input())

field = [[0] * (N) for _ in range(N)]

delta_row = [-1, 0, 1, 0]
delta_col = [0, 1, 0, -1]  # 북[0], 동[1], 남[2], 서[3]

for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    field[a][b] = 1

zipfield = list(zip(*field))

for i in range(N):
    for j in range(N):
        field[i][j] += zipfield[i][j]

for i in range(N):
    field[i][i] = 1

right = []
up = []

# 오른쪽 끝에 도달
# for stdnt1 in range(N):
#     row = stdnt1
#     col = stdnt1
#
#     if 0 <= row + delta_row[1] < N and 0 <= col + delta_col[1] < N:
#
#         while True:
#             if field[row + delta_row[1]][col + delta_col[1]] == 1:
#                 row = row + delta_row[1]
#                 col = col + delta_col[1]
#             elif field[row + delta_row[2]][col + delta_col[2]] == 1:
#                 row = row + delta_row[2]
#                 col = col + delta_col[2]
#             elif field[row + delta_row[1] + delta_row[2]][col + delta_col[1] + delta_col[2]] == 1:
#                 row = row + delta_row[1] + delta_row[2]
#                 col = col + delta_col[1] + delta_col[2]
#
#             if col == N + 1:
#                 right.append(stdnt1)
#                 break
#
# # 위쪽 끝에 도달
# for stdnt2 in range(N):
#     row = stdnt2
#     col = stdnt2
#
#     if 0 <= row + delta_row[1] < N and 0 <= col + delta_col[1] < N:
#
#         while True:
#             if field[row + delta_row[0]][col + delta_col[0]] == 1:
#                 row = row + delta_row[0]
#                 col = col + delta_col[0]
#             elif field[row + delta_row[3]][col + delta_col[3]] == 1:
#                 row = row + delta_row[3]
#                 col = col + delta_col[3]
#             elif field[row + delta_row[0] + delta_row[3]][col + delta_col[0] + delta_col[3]] == 1:
#                 row = row + delta_row[0] + delta_row[3]
#                 col = col + delta_col[0] + delta_col[3]
#
#             if col == N + 1:
#                 up.append(stdnt2)
#                 break

for k in range(N):
    print(field[k])
