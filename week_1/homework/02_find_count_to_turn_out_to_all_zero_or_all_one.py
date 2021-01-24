input = "10001100111110"


def find_count_to_turn_out_to_all_zero_or_all_one(string):
    # 이 부분을 채워보세요!
    cnt = [0] * 2
    result = 0
    for i in range(0, len(string)-1):
        # print(string[i])
        if int(string[i]) == 0:
            if string[i] != string[i+1]:
                cnt[0] += 1
        else:
            if string[i] != string[i+1]:
                cnt[1] += 1
        if cnt[0] > cnt[1]:
            result = cnt[0]
        else:
            result = cnt[1]
    return result


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)