# Python 내장 함수 set, sum 등 사용 시 감점

def analyze_items(items_list):

    new_lst = []  # 중복 없는 list를 만들기 위해 빈 list를 생성.
    positive_sum = 0  # 양수 합을 구하기 위해 인수를 생성.
    negative_sum = 0  # 음수 합을 구하기 위해 인수를 생성.
    items_list.sort()  # 아래 while 문이 만족할 수 있도록 items_list를 정렬.

    while items_list != []:  # items_list에서 요소를 전부 뽑아낼 때까지 반복.

        el = items_list.pop(0)  # 첫 번째 요소를 뽑아서 인수로 설정.        

        for _ in range(len(items_list)):  # 남은 items_list의 길이만큼 반복
            if el == items_list[0]:  # 남은 items_list의 첫 요소와 pop한 요소가 같다면 items_list에서 제거.
                items_list.remove(el)  # 이 때, 요소가 무질서하게 들어있다면 오류가 나기 때문에 먼저 정렬을 해 줌.
        
        new_lst.append(el)  # 중복 없는 새 list를 만들어 줌.
    
    for el in new_lst:
        if type(el) == int:  # 숫자만 판별
            if el > 0:
                positive_sum += el
            else:
                negative_sum += el  # 양수일 때 positive_sum에 더함, 아닐 때 negative_sum에 더함. 0일 때는 어느 쪽에 더해도 영향이 없으므로 고려하지 않아도 됨.

    return (new_lst, (positive_sum, negative_sum))  # 필요한 요소를 반환.

print(analyze_items([2, 2, 2, "a", "a", 3, 0, -2]))
# 예시 결과: ([2, "a", 3, 0, -2], (5, -2))

print(analyze_items([]))
# 예시 결과: ([], (0, 0))

print(analyze_items(["apple", "apple", "banana"]))
# 예시 결과: (["apple", "banana"], (0, 0))