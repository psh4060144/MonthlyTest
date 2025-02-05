############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
def find_max_position(matrix):

    max_num = 0  # 가장 큰 값을 찾아 그 위치를 찾기 위해 가장 큰 값을 넣을 인수를 설정.
    max_num_point = []  # 위치를 list 형태로 반환하기 위해 빈 list를 설정.

    for row_num in range(len(matrix)):  # 행 갯수만큼 반복하여 행 위치를 먼저 설정
        for column_num in range(len(matrix[row_num])):  # 열 갯수만큼 반복하여 열 위치를 설정.
            if matrix[row_num][column_num] > max_num:  # 행, 열에 위치한 수와 가장 큰 값을 넣은 수를 비교하여,
                max_num = matrix[row_num][column_num]  # 더 크다면 그 값을 할당하고,
                max_num_point = [row_num, column_num]  # 빈 list 또한 위치값으로 재할당.

    return max_num_point  # 행, 열로 이루어진 list 반환.
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

matrix3 = [
    [9, 2, 5],
    [4, 9, 6],
    [7, 8, 1]
]
#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(find_max_position(matrix1))  # [2, 2]
print(find_max_position(matrix2))  # [0, 0]
print(find_max_position(matrix3))  # [0, 0]
#####################################################
