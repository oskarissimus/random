def merge_sort(l: list[int]) -> list[int]:
    if l == []:
        return []
    if len(l) == 1:
        return l[:]
    mid = len(l) // 2
    l1 = l[:mid]
    l2 = l[mid:]
    l1_sorted = merge_sort(l1)
    l2_sorted = merge_sort(l2)
    l_sorted = merge(l1_sorted, l2_sorted)
    return l_sorted


def merge(l1: list[int], l2: list[int]):
    i1 = 0
    i2 = 0

    merged: list[int] = []

    while i1 < len(l1) and i2 < len(l2):
        if l1[i1] < l2[i2]:
            merged.append(l1[i1])
            i1 += 1
        else:
            merged.append(l2[i2])
            i2 += 1

    if i1 == len(l1):
        merged += l2[i2:]
    else:
        merged += l1[i1:]

    return merged
