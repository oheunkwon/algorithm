def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
    # 이 부분을 채워보세요!
    for idx in string:
        # print(idx.isalpha())
        if not idx.isalpha():
            continue
        aoa_idx = ord(idx)-ord('a')
        alphabet_occurrence_array[aoa_idx] += 1
    return alphabet_occurrence_array


print(find_alphabet_occurrence_array("hello my name is sparta"))