T = int(input())  # test case 입력.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N = int(input()) + 1  # 콘센트 갯수 N. 계산의 편의성을 위해 차단기도 갯수에 포함한다.
    arr = [(0, 0)] + [tuple(map(int, input().split())) for _ in range(N - 1)]  # 콘센트와 차단기의 좌표를 tuple 로 입력.
    new_arr = []  # 전선 길이를 구하기 위해 빈 list 를 제작.

    for i in range(N - 1):
        for j in range(i + 1, N):  # 모든 부분집합에 대해
            # 서로 이어진 콘센트 번호와 전선 길이를 tuple로 입력. 차단기 번호는 0.
            new_arr += [(i, j, abs(arr[i][0] - arr[j][0]) + abs(arr[i][1] - arr[j][1]))]

    # Kruskal algorithm.
    new_arr.sort(key=lambda x: x[2])  # 전선 길이 순으로 정렬.
    length = 0  # 최종 전선의 길이를 구하기 위해 변수를 설정.
    union = [None] * N  # 이어져 있는 콘센트들의 대표를 적어주기 위해 None 으로 이루어진 list 제작.
    cnt = 0  # 최소 전선 갯수가 N - 1 개이므로 전선 갯수를 세는 변수를 설정.

    for k in range(len(new_arr)):  # 전선 길이가 짧은 콘센트들부터 순회하면서

        # 각 콘센트의 대표가 없다면 본인이 대표를 하고, 있다면 패스.
        if union[new_arr[k][0]] is None:
            union[new_arr[k][0]] = new_arr[k][0]
        if union[new_arr[k][1]] is None:
            union[new_arr[k][1]] = new_arr[k][1]

        if union[new_arr[k][0]] != union[new_arr[k][1]]:  # 서로 대표가 다르다면
            length += new_arr[k][2]  # 둘을 이어 최종 전선 길이에 추가하고
            cnt += 1  # 전선 갯수에 1 추가.

            # 두 콘센트 중 더 작은 번호의 콘센트를 대표로 설정.
            if union[new_arr[k][0]] >= union[new_arr[k][1]]:
                big, small = union[new_arr[k][0]], union[new_arr[k][1]]
            else:
                small, big = union[new_arr[k][0]], union[new_arr[k][1]]

            for l in range(N):  # 대표 list 를 순회하면서
                if union[l] == big:
                    union[l] = small  # 대표 번호를 교체.

        if cnt == N - 1:  # 최소 전선 갯수에 도달하면
            break  # 종료.

    print(f'#{tc} {length}')  # 양식에 맞게 출력.



