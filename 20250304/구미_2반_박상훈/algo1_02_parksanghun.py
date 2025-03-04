T = int(input())  # test case 갯수 입력

for tc in range(1, T + 1):  # test case 만큼 반복. 양식에 맞게 출력하기 위해 tc의 범위를 설정해 줌.

    N, M = map(int, input().split())
    team = list(map(int, input().split()))  # 주어진 정보 입력.

    for i in range(M):  # M 번의 명령이 입력됨.
        a, b, c = map(int, input().split())  # 각 변수를 입력.
        b -= 1  # indexing 은 0부터 시작이지만 사람은 1번부터 시작하므로 위치를 한 칸 당겨 줌.

        for j in range(1, c + 1):  # 변하는 범위를 설정하여 그 범위만큼 반복.
            if b - j >= 0 and b + j < N:  # 사람이 범위 내에 있고
                if team[b - j] == team[b + j]:  # 양쪽 사람이 같은 상태라면
                    team[b - j] = 1 - team[b - j]
                    team[b + j] = 1 - team[b + j]  # 각각 상태를 바꿔줌.

    print(f'#{tc}', end=' ')
    print(*team, end=' ')
    print()  # 양식에 맞게 출력.