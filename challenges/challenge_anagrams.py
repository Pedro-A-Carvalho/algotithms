def is_anagram(first_string, second_string):
    """Faça o código aqui."""
    first_string = "".join(merge_sort(first_string.lower()))
    second_string = "".join(merge_sort(second_string.lower()))
    if first_string == "" or second_string == "":
        return (first_string, second_string, False)
    return (first_string, second_string, first_string == second_string)


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged
