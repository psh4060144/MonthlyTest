def findingstart(maze):  # 미로의 시작점을 찾는 함수
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:  # 미로의 시작점을 찾아 그 좌표를 return.
                return i, j


def bfs(start_row, start_col):  # 미로를 탐색하는 함수. BFS 이용.
    queue = [(start_row, start_col, 0)]  # queue 에 (행, 열, 이동횟수)를 입력.
    visited = [[0] * N for _ in range(N)]  # 방문 확인용 2차원 list 를 만들어서
    visited[start_row][start_col] = 1  # 방문한 위치에 표시.
    d_row = [-1, 0, 1, 0]
    d_col = [0, 1, 0, -1]  # 4방향 delta 검색을 위해 상, 우, 하, 좌의 방향 설정.

    while queue:  # queue 가 빌 때까지 반복.
        current = queue.pop(0)  # queue 에서 가장 앞의 값을 추출.

        if maze[current[0]][current[1]] == 4:  # 현재 점프대에 있다면
            for i in range(4):  # 4방향을 돌아보면서 확인하는데,
                if 0 <= current[0] + d_row[i] * 2 < N and 0 <= current[1] + d_col[i] * 2 < N:  # 점프대이므로 한 칸 뛰어 넘은 칸이 범위 내(미로 안)에 있는지 확인.
                    if maze[current[0] + d_row[i] * 2][current[1] + d_col[i] * 2] != 1 and visited[current[0] + d_row[i] * 2][current[1] + d_col[i] * 2] == 0:  # 벽이 아니고 가지 않은 땅이라면
                        queue.append((current[0] + d_row[i] * 2, current[1] + d_col[i] * 2, current[2] + 1))  # queue 에 (현재 위치 행, 현재 위치 열, 이동 횟수 + 1)을 삽입.
                        visited[current[0] + d_row[i] * 2][current[1] + d_col[i] * 2] = 1  # 이후 방문 표시.

                    if maze[current[0] + d_row[i] * 2][current[1] + d_col[i] * 2] == 3:  # 만약 확인한 곳이 도착지라면
                        return current[2] + 2  # 이동 횟수 출력. 출발지와 도착지를 세지 않았으므로 2를 더해야 한다.
        else:  # 점프대가 아니라면
            for i in range(4):  # 4방향을 돌아보면서 확인하는데, 미로가 벽으로 둘러쌓여 있으므로 범위 내(미로 안)에 있는지 확인할 필요는 없다.
                if maze[current[0] + d_row[i]][current[1] + d_col[i]] != 1 and visited[current[0] + d_row[i]][current[1] + d_col[i]] == 0:  # 벽이 아니고 가지 않은 땅이라면
                    queue.append((current[0] + d_row[i], current[1] + d_col[i], current[2] + 1))  # queue 에 (현재 위치 행, 현재 위치 열, 이동 횟수 + 1)을 삽입.
                    visited[current[0] + d_row[i]][current[1] + d_col[i]] = 1  # 이후 방문 표시.

                if maze[current[0] + d_row[i]][current[1] + d_col[i]] == 3:  # 만약 확인한 곳이 도착지라면
                    return current[2] + 2  # 이동 횟수 출력. 출발지와 도착지를 세지 않았으므로 2를 더해야 한다.

    return -1  # 모든 곳을 확인했는데 도착지에 도착하지 못했다면 -1을 출력.


T = int(input())  # test case

for tc in range(1, T + 1):  # test case 만큼 반복

    N = int(input())  # 미로 크기 입력
    maze = [list(map(int, input().split())) for _ in range(N)]  # 미로의 형태를 입력

    start_row, start_col = findingstart(maze)  # findingstart 함수를 통해 미로의 출발점을 확인.
    count = bfs(start_row, start_col)  # 이후 bfs 함수를 통해 미로를 풀어낸다.

    print(f'#{tc} {count}')  # 양식에 맞게 출력.
