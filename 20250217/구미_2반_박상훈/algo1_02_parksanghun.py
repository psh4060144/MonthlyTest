T = int(input())  # test case 갯수

for tc in range(1, T + 1):  # test case 갯수만큼 반복. print 때의 test case 번호를 위해 1 ~ T + 1 까지 순회.

    N, M = map(int, input().split())  # N 명의 사람, M 번의 명령.
    line = list(map(int, input().split()))  # 팀원들의 현재 상태를 받음.

    for i in range(M):
        order = list(map(int, input().split()))  # [0]: 상태 변화 유무 / [1]: 시작 위치 / [2]: 변화하는 명 수.
        start = order[1] - 1  # 팀원이 1번부터 시작이기에 0부터 시작할 수 있도록 변수를 설정해줌.
        if start + order[2] > N:  # 변화하는 명 수가 범위를 넘어가면 line 끝까지 변화하는 것으로 설정.
            end = N
        else:
            end = start + order[2]  # 넘어가지 않으면 그냥 진행.

        for j in range(start, end):
            line[j] = (line[j] + order[0]) % 2  # 범위 내에서 상태 변화.
            # 상태가 변화한다면(order[0] == 1) 모든 0을 1로, 모든 1을 0으로. 상태가 변화하지 않는다면(order[0] == 0) 변화하지 않음.

    print(f'#{tc}', end=' ')  # 조건에 맞게 출력.
    for k in range(len(line)):
        print(line[k], end=' ')
    print()
