def count_matching_numbers(list_1, list_2):
    count = 0

    for num in list_1:
        if num in list_2:
            count += 1

    return count


print(count_matching_numbers([2, 7, 11, 14, 25, 40], [2, 11, 13, 14, 30, 35]))
print(count_matching_numbers([2, 7, 11, 14, 25, 40], [14]))