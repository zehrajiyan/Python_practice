def deep_reverse(lst):
    reversed_list = []
    for item in reversed(lst):
        if isinstance(item, list):
            reversed_list.append(deep_reverse(item))  # iç listeyi de ters çevir
        else:
            reversed_list.append(item)
    return reversed_list


input_list = [[1, 2], [3, 4], [5, 6, 7]]
output = [deep_reverse(input_list)]
print(output)