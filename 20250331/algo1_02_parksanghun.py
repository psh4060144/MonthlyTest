T = int(input())  # test case 갯수 입력.
for tc in range(1, T + 1):  # test case 만큼 반복.

    o, e = map(int, input().split())  # 여는 시간 o, 닫는 시간 e.
    N = int(input())  # 신청 팀 수 N

    arr = []  # 모든 팀을 정렬하기 위해 빈 list 를 만들어줌.
    for i in range(N):  # 팀 수만큼 반복하면서
        Si, Fi = map(int, input().split())  # 희망 시작시간 Si, 희망 종료시간 Fi 를 입력.
        arr.append((Si, Fi))  # list 에 tuple 형태로 추가해 줌.
    arr.sort(key=lambda x: x[1])  # 모든 데이터를 받았다면 희망 종료시간을 기준으로 정렬.

    start = N  # 시작 위치를 정하기 위해 팀의 갯수를 변수로 설정.
    new_arr = []  # 이용할 수 있는 팀을 정리하기 위해 빈 list 를 설정.

    for j in range(N):  # 종료 시간이 빠른 팀부터 순회하면서,
        if arr[j][0] >= o and arr[j][1] <= e:  # 여는 시간과 닫는 시간 사이에 이용하는 팀이라면
            start = j  # 그 팀의 위치를 시작 위치로 잡고
            new_arr.append(arr[j])  # 그 팀을 이용할 수 있다고 판단.
            break  # 이용할 수 있는 팀을 찾았다면 종료.

    for k in range(start, N):  # 시작 위치부터 끝까지 순회하면서,
        if arr[k][0] >= new_arr[-1][1] and arr[k][1] <= e:  # 시작 시간이 이용할 수 있는 팀의 종료 시간 이후이고, 종료 시간이 닫는 시간 이전이라면
            new_arr.append(arr[k])  # 그 팀을 이용할 수 있다고 판단.

    print(f'#{tc} {len(new_arr)}')  # 이용할 수 있는 팀의 정리가 끝났다면 양식에 맞게 출력.
