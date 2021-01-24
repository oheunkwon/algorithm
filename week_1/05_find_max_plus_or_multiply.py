input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    # 이 부분을 채워보세요!
    # result = 0
    # for i in array:
    #     if i == 0 or i == 1:
    #         result += i
    #         if result == 0:
    #             result += 1
    #     else:
    #         if result == 0:
    #             result += 1
    #         result *= i
    #
    # return result
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number

    return multiply_sum



result = find_max_plus_or_multiply(input)
print(result)