def preorder(v):  # 전위 순회 함수.
    global pre_binary  # 전위 순회한 문자열을 만들기 위해 전역 변수를 사용.
    pre_binary += value[v]  # 문자열에 해당 노드의 값을 추가.
    if v * 2 <= N:  # 자식이 있고, 왼쪽 노드라면
        preorder(v * 2)  # 왼쪽 자식으로 이동.
    if v * 2 + 1 <= N:  # 자식이 있고, 오른쪽 노드라면
        preorder(v * 2 + 1)  # 오른쪽 자식으로 이동.


def inorder(v):  # 중위 순회 함수.
    global in_binary  # 중위 순회한 문자열을 만들기 위해 전역 변수를 사용.
    if v * 2 <= N:  # 자식이 있고, 왼쪽 노드라면
        inorder(v * 2)  # 왼쪽 자식으로 이동.
    in_binary += value[v]  # 문자열에 해당 노드의 값을 추가.
    if v * 2 + 1 <= N:  # 자식이 있고, 오른쪽 노드라면
        inorder(v * 2 + 1)  # 오른쪽 자식으로 이동.


def postorder(v):  # 후위 순회 함수.
    global post_binary  # 후위 순회한 문자열을 만들기 위해 전역 변수를 사용.
    if v * 2 <= N:  # 자식이 있고, 왼쪽 노드라면
        postorder(v * 2)  # 왼쪽 자식으로 이동.
    if v * 2 + 1 <= N:  # 자식이 있고, 오른쪽 노드라면
        postorder(v * 2 + 1)  # 오른쪽 자식으로 이동.
    post_binary += value[v]  # 문자열에 해당 노드의 값을 추가.


def calc(binary):  # 이진수 str 을 받아 10진수로 변환하는 함수.
    result = 0  # 결과값을 출력하기 위해 변수를 설정.
    for i in range(N):  # 이진수를 순회하면서
        result += int(binary[i]) * 2 ** (N - 1 - i)  # 해당 자리의 10진수 값을 결과값에 합산.
    return result  # 결과값을 출력.


T = int(input())  # test case.
for tc in range(1, T + 1):  # test case 만큼 반복.
    N = int(input())  # 정점 갯수를 입력.
    value = [0] + input().split()  # 정점의 값을 해당 정점 번호에 입력하기 위해 list 앞에 0을 추가해서 정보를 받음.

    pre_binary = ''
    in_binary = ''
    post_binary = ''  # 전위, 중위, 후위 순회로 이진수 str 을 제작하기 위해 빈 str 을 설정.

    preorder(1)
    inorder(1)
    postorder(1)  # 전위, 중위, 후위 순회 실행.

    pre_result = calc(pre_binary)
    in_result = calc(in_binary)
    post_result = calc(post_binary)  # 만들어진 이진수 str 을 10진수로 변환.

    print(f'#{tc} {max(pre_result, in_result, post_result)}')  # 가장 큰 값을 형식에 맞게 출력.
