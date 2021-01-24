input = "hello my name is sparta"


def find_max_occurred_alphabet(string):
    # 이 부분을 채워보세요!
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "n"]
    alphabet_occurence = [0] * 26
    for i in string:
        if not i.isalpha():
            continue
        arr_idx = ord(i) - ord('a')
        alphabet_occurence[arr_idx] += 1

    max_occur = 0
    # print(max_occur)
    for i in alphabet_occurence:
        idx = alphabet_occurence.index(i)
        print("idx",idx)
        if i > max_occur:
            max_occur = idx
            print(idx)
        # print(alphabet_occurence[i])
    return chr(idx + ord('a'))


result = find_max_occurred_alphabet(input)
print(result)
