############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
def point_sum(matrix, row_num, column_num):  # 상하좌우의 값을 더하는 함수.

    if row_num -1 < 0:  # 범위를 벗어나는 값은 0으로 처리.
        left = 0
    else: left = matrix[row_num -1][column_num]

    if row_num +1 > len(matrix):  # 범위를 벗어나는 값은 0으로 처리.
        right = 0
    else: right = matrix[row_num + 1][column_num]

    if column_num -1 < 0:  # 범위를 벗어나는 값은 0으로 처리.
        up = 0
    else: up = matrix[row_num][column_num -1]

    if column_num +1 > len(matrix):  # 범위를 벗어나는 값은 0으로 처리.
        down = 0
    else: down = matrix[row_num][column_num + 1]
        
    return left + right + up + down

def max_adjacent_sum(matrix):

    matrix_sum = 0
    point_index = []

    for row_num in range(len(matrix)):  # 행 갯수만큼 반복하여 행 위치를 먼저 설정
        for column_num in range(len(matrix[row_num])):  # 열 갯수만큼 반복하여 열 위치를 설정.
            all_sum = point_sum(matrix, row_num, column_num)  # 위에서 만들었던 상하좌우를 더하는 함수를 실행.
            if all_sum > matrix_sum:
                matrix_sum = all_sum  # 더 큰 수가 들어올때까지 반복하여여
                point_index = [row_num, column_num]  # 해당 위치를 반환.

    return point_index
    # 여기에 코드를 작성하여 함수를 완성합니다.


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

# 예시 행렬 데이터
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(max_adjacent_sum(matrix1))  # 29
print(max_adjacent_sum(matrix2))  # 25
#####################################################
