T = int(input())

for tc in range(1, T + 1):

    N = int(input())

    field = [list(map(int, input().split())) for _ in range(N)]

    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]  # 북, 동, 남, 서
    count_max = 0

    for row in range(N):
        for col in range(N):
            count = 1
            ROW = row
            COL = col

            while True:
                goto = field[ROW][COL]
                goto_dir = None

                for d in range(4):
                    if 0 <= ROW + delta_row[d] < N and 0 <= COL + delta_col[d] < N:
                        if goto > field[ROW + delta_row[d]][COL + delta_col[d]]:
                            goto = field[ROW + delta_row[d]][COL + delta_col[d]]
                            goto_dir = d

                if goto_dir == None:
                    break
                else:
                    ROW = ROW + delta_row[goto_dir]
                    COL = COL + delta_col[goto_dir]
                    count += 1

            if count_max < count:
                count_max = count

    print(f'#{tc} {count_max}')
