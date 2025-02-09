# Python 내장함수 sum, len, min, max, sorted 또는 리스트 sort 메서드 사용 시 감점

def analyze_likes(weekly_like_list):

    # 좋아요 수의 평균을 실수로 반환.
    like_sum = 0  # 먼저 총합을 구하기 위해 총합을 0으로 설정.
    for el in weekly_like_list:
        like_sum += el  # list의 모든 값을 더함.
    like_average = like_sum / 7  # 총합을 7로 나누면 평균을 구할 수 있고, 이 평균을 반환하면 됨.
    
    # 가장 많은 좋아요 수와 가장 적은 좋아요 수의 차이를 반환.    
    list_max = weekly_like_list[0]
    list_min = weekly_like_list[0]  # 먼저 가장 큰 요소와 가장 작은 요소를 구하기 위해 각 요소를 list의 첫 번째 요소로 할당.

    for el in weekly_like_list:
        if el > list_max:
            list_max = el  # list의 요소를 비교해가면서 list_max보다 크다면 list_max의 값을 el로 변경. 이를 통해 list의 가장 큰 수가 list_max로 할당됨.
        else:
            pass

    for el in weekly_like_list:
        if el < list_min:
            list_min = el  # 위와 마찬가지로 가장 작은 수를 list_min으로 할당할 수 있음.
        else:
            pass
    
    max_minus_min = list_max - list_min  # 가장 큰 요소와 가장 작은 요소를 구했으므로 이 둘의 차이만큼을 반환하면 됨.

    return (like_average, max_minus_min)  # 평균, 그리고 가장 큰 값과 가장 작은 값의 차이를 반환.


analyze_likes([2, 5, 3, 8, 0, 10, 4])
# 1) 평균 = (2 + 5 + 3 + 8 + 0 + 10 + 4) / 7
#    = 32 / 7 ≈ 4.5714...
# 2) 최소=0, 최대=10, 차이=10
# 결과: (4.5714..., 10)
print(analyze_likes([2, 5, 3, 8, 0, 10, 4]))  # 예시: (4.5714..., 10)
print(analyze_likes([7, 7, 7, 7, 7, 7, 7]))   # (7.0, 0)