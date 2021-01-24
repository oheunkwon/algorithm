finding_target = 2
finding_numbers = [0, 3, 5, 6, 1, 2, 4]


def is_exist_target_number_binary(target, numbers):
    # 이 부분을 채워보세요!
    current_min = 0
    current_max = len(numbers) - 1
    numbers_sorted = sorted(finding_numbers)

    current_guess = (current_max + current_min) // 2

    while current_min <= current_max:
        if numbers_sorted[current_guess] == target:
            return True
        elif numbers_sorted[current_guess] < target:
            current_min = current_guess + 1
        else:
            current_max = current_guess - 1
        # 구현해보세요!
        current_guess = (current_max + current_min) // 2
    return False


result = is_exist_target_number_binary(finding_target, finding_numbers)
print(result)