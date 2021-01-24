shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두", "사이다", "콜라", "아이스크립"]


def is_available_to_order(menus, orders):
    # 이 부분을 채워보세요!
    available_array = [0] * len(orders)
    # while available_array == shop_orders:
    for i in range(len(menus)):
        for j in range(len(orders)):
            if menus[i] == orders[j]:
                available_array[j] = orders[j]
    if available_array == orders:
        return True
    else:
        return False


result = is_available_to_order(shop_menus, shop_orders)
print(result)
























