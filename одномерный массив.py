def sum_negative_between_min_max(arr):
    if len(arr) < 3:
        return 0

    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    start = min(min_index, max_index) + 1
    end = max(min_index, max_index)

    middle_elements = arr[start:end]

    negative_elements = [x for x in middle_elements if x < 0]

    return sum(negative_elements)

A = [4, -2, 3, -5, 7, -1, 8, 0]
result = sum_negative_between_min_max(A)
print("Сумма отрицательных элементов между min и max:", result)
