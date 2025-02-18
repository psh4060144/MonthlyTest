T = int(input())  # test case 갯수

for tc in range(1, T + 1):  # test case 갯수만큼 반복. print 때의 test case 번호를 위해 1 ~ T + 1 까지 순회.

    monster = int(input())  # 정보를 받지만, 쓰지는 않음.

    old_field = [list(map(int, input())) for _ in range(10)]  # 해당 지역의 정보를 받음.
    new_field = [[0] * 10 for _ in range(10)]  # 광선을 표시하기 위해 새 지역을 만듦.

    delta_row = [-1, 0, 1, 0]
    delta_col = [0, 1, 0, -1]  # 북, 동, 남, 서의 delta.

    for row in range(10):
        for col in range(10):
            if old_field[row][col] != 0:  # 0이 아닌 곳은 괴물이나 벽이 있다는 뜻.
                new_field[row][col] = old_field[row][col] * 10  # 모든 괴물과 벽을 표시해 주는데, 괴물과 벽임을 표시하기 위해 10을 곱해준다.

    for row in range(10):
        for col in range(10):
            if old_field[row][col] != 0 and old_field[row][col] != 4:  # 이후 괴물만 찾아 그 괴물에서 발사된 광선을 표시.
                for delta in range(4):  # 괴물이 4방향으로 광선을 발사하므로 4방향을 돌면서 먼저 방향을 설정.
                    for multiply in range(1, old_field[row][col] + 1):  # 방향을 설정한 후에 광선을 그려 나감. 광선의 길이만큼 색칠하는데, 괴물 자신의 자리에는 칠하지 않음.

                        ROW = row + delta_row[delta] * multiply
                        COL = col + delta_col[delta] * multiply  # 광선이 뻗어나가는 방향, 길이를 새 변수로 설정.

                        if 0 <= ROW < 10 and 0 <= COL < 10:  # 해당 지역 내에서만 표시하기 위해 범위를 잡아 줌.
                            if new_field[ROW][COL] > 3:  # 벽을 만나거나 괴물을 만나면 광선이 멈추므로 색칠을 즉시 종료한 후 다음 방향에서 새로 시작.
                                break
                            else:
                                new_field[ROW][COL] = old_field[row][col]  # 만나지 않는다면 광선 길이만큼 같은 색을 칠해 줌.

    count = 0  # 안전한 구역을 세기 위해 변수를 설정.

    for row in range(10):
        for col in range(10):
            if new_field[row][col] == 0:  # 안전한 구역은 0이 적혀 있으므로 모든 0의 갯수를 세 줌.
                count += 1

    print(f'#{tc} {count}')  # 조건에 맞게 출력.
