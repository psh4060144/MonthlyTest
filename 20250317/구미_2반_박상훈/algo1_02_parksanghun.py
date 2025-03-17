T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.

    N, K = map(int, input().split())  # 이진수의 자릿수 N, 싸피 이진수 내의 1의 갯수 K 을 입력.
    binary = input()  # 이진수를 str 형식으로 입력.
    cnt_max = 0  # 최대 길이를 구하기 위해 변수를 설정.

    for i in range(N - 1):  # 싸피 이진수의 시작점이 될 수 있는 부분만 반복.
        count = 0  # 매 반복마다 해당 이진수의 길이를 세기 위해 변수를 설정.
        tmp = K  # 싸피 이진수 내의 1의 갯수를 세기 위해 새 변수를 할당.

        if binary[i] == '1':  # 시작점이 1인 경우에만 탐색.

            for j in range(i, N):  # 싸피 이진수의 종료점이 될 수 있는 부분만 반복.
                count += 1  # 해당 이진수의 길이를 세기 시작함.

                if binary[j] == '1':  # 1을 만날 때마다 tmp 에서 1을 빼 줌.
                    tmp -= 1

                if tmp == 0:  # 싸피 이진수 내의 1의 갯수를 충족했다면
                    break  # 그대로 종료.

            else:  # 싸피 이진수 내의 1의 갯수를 충족하지 못했다면
                tmp = K  # tmp 를 초기 상태로 되돌리고
                count = 0  # 해당 이진수의 길이도 0으로 초기화.

            if cnt_max < count:  # 싸피 이진수의 길이와 최대 길이를 비교하여
                cnt_max = count  # 싸피 이진수가 더 길다면 최대 길이를 갱신.

    print(f'#{tc} {cnt_max}')  # 형식에 맞게 출력.
