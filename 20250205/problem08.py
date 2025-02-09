# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.

def max_adjacent_sum(matrix):

    N = len(matrix)
    around_row = [-1, 1, 0, 0, 0]
    around_col = [0, 0, -1, 1, 0]
    sum_max = 0
    
    for row in range(len(around_row)):
        for col in range(len(around_row)):
            sum = 0
            
            for i in range(5):
                
                if 0 <= row + around_row[i] < N and 0 <= col + around_col[i] < N:
                    sum += matrix[row + around_row[i]][col + around_col[i]]
                
                if sum_max < sum:
                    sum_max = sum

    return sum_max

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

print(max_adjacent_sum(matrix1))  # 29
print(max_adjacent_sum(matrix2))  # 25