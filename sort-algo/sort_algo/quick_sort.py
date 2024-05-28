def quick_sort(l: list[int]):
    if l == []:
        return []
    if len(l) == 1:
        return l[:]
    pivot = l[0]
    left = [x for x in l[1:] if x < pivot]
    right = [x for x in l[1:] if x >= pivot]
    left_sorted = quick_sort(left)
    right_sorted = quick_sort(right)
    return left_sorted + [pivot] + right_sorted
