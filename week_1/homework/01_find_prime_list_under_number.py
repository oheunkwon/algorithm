input = 20


def find_prime_list_under_number(number):
    # 이 부분을 채워보세요!
    prime_array = []
    for i in range(2, number):
        status = True
        for j in range(2, i):
            if i % j == 0:
                status = False
                break
        if status:
            prime_array.append(i)

    return prime_array


result = find_prime_list_under_number(input)
print(result)