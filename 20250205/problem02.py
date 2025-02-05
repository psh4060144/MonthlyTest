############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def analyze_treasures(treasure_list, threshold):

    treasure_dict = {}  # 보물 갯수 dict를 생성하기 위해 빈 dict를 생성.
    threshold_sum = 0  # 임계값을 초과하는 보물 수를 세기 위해 해당 변수를 설정.
    
    for el1 in treasure_list:

        treasure_count = 0  # 보물 갯수를 세기 위해 해당 변수를 설정.

        for el2 in treasure_list:  # 중첩 반복문을 이용해 해당 인수가 list에 몇 개 들어있는 지 셈.
            if el1 == el2:
                treasure_count += 1  # 같은 값이 있는 만큼(들어있는 갯수만큼) treasure_count에 할당이 됨.
        
        treasure_dict[el1] = treasure_count  # dict에 인수:갯수로 이루어진 key:value 쌍을 추가. 

    for keys in treasure_dict:  # 만들어진 dict를 바탕으로 임계값을 초과하는 갯수를 판단.
        if treasure_dict[keys] > threshold:  # dict의 모든 value는 숫자이므로 바로 임계값과 비교할 수 있음.
            threshold_sum += 1  # 임계값보다 더 큰 값의 갯수만큼 threshold_sum에 할당이 됨.

    return (treasure_dict, threshold_sum)  # 만든 dict와 임계값을 초과하는 갯수를 반환.

    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 테스트 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(analyze_treasures(["gold", "silver", "gold", "diamond", "coin", "coin"], 1))
# ({'gold': 2, 'silver': 1, 'diamond': 1, 'coin': 2}, 2)

print(analyze_treasures([], 3))
# ({}, 0)

print(analyze_treasures(["pearl", "pearl", "ruby"], 2))
# ({'pearl': 2, 'ruby': 1}, 0)
#####################################################
