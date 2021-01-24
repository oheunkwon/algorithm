input = [3, 5, 6, 1, 2, 4]


def is_number_exist(number, array):
    # 이 부분을 채워보세요!
    for i in array: # array 길이만큼 연산
        if i == number: # 비교연산 1번
            return True # N * 1

    return False


result = is_number_exist(3, input)
print(result)