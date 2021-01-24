input = "abczfcabade"


def find_not_repeating_character(string):
    # 이 부분을 채워보세요!
    alphabet_occurrence_array = [0] * 26

    # for char in string:
    #     if not char.isalpha():
    #         continue
    # arr_index = ord(char) - ord("a")
    # alphabet_occurrence_array[arr_index] += 1
    #
    # not_repeating_character_array = []
    # for index in range(len(alphabet_occurrence_array)):
    #     alphabet_occurrence = alphabet_occurrence_array[index]
    #
    #     if alphabet_occurrence == 1:
    #         not_repeating_character_array.append(chr(index + ord("a")))
    # for char in string:
    #     if char in not_repeating_character_array:
    #         return char
    # return char

    # 이 부분을 채워보세요!
    for i in string:
        # print(idx.isalpha())
        arr_idx = ord(i) - ord('a')
        alphabet_occurrence_array[arr_idx] += 1
    for i in range(len(alphabet_occurrence_array)):
        for alpha in string:
            idx = ord(alpha)-ord('a')
            if alphabet_occurrence_array[idx] == 1:
                return chr(idx+ord('a'))
        if not alphabet_occurrence_array[i] == 1:
            continue
        real_idx = i + ord('a')
        return chr(real_idx)


result = find_not_repeating_character(input)
print(result)