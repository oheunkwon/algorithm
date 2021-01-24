input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26
    # 이 부분을 채워보세요!
    for idx in string:
        # print(idx.isalpha())
        if not idx.isalpha():
            continue
        aoa_idx = ord(idx)-ord('a')
        alphabet_occurrence_array[aoa_idx] += 1

    max_occurence = 0
    max_alphabet_index = 0
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurence:
            max_alphabet_index = index
            max_occurence = alphabet_occurrence

    max = max_alphabet_index + ord('a')
    return chr(max)


result = find_max_occurred_alphabet(input)
print(result)