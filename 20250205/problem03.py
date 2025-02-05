############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def find_most_populated(animal_map):

    max_animal = 0  # 가장 많은 동물의 수를 찾기 위해 인수를 설정.
    max_animal_name = None  # 가장 많은 동물의 이름을 찾기 위해 인수를 설정. 동물 정보가 없을 때를 위해 기본값을 None으로 설정.

    if len(animal_map) == 0:  # 빈 딕셔너리이거나 동물 정보가 없다면 이름 그대로(None) 반환.
        pass
    else:
        for keys in animal_map:
            if animal_map[keys] > max_animal:  # dict의 value가 가장 큰 값을 찾는 if문. value가 같다면 첫 이름을 쓰기 위해 >(초과)로 설정.
                max_animal = animal_map[keys]  # 가장 큰 값을 찾는 이유: 다른 value와 비교하기 위해.
                max_animal_name = keys  # 가장 큰 value를 찾을 때마다 동물의 이름이 새로 할당됨.

    return f'{max_animal_name}'  # 동물의 이름을 반환.
    # 여기에 코드를 작성하여 함수를 완성합니다.

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(find_most_populated({"lion": 5, "tiger": 3, "elephant": 10}))  # 예시: "elephant"
print(find_most_populated({}))                                       # None
print(find_most_populated({"wolf": 4, "wolfdog": 4, "hyena": 4}))     # "wolf"
#####################################################
