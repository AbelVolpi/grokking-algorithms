def binary_search(list, item):
    first = 0
    last = len(list) - 1
    while first <= last:
        mid = (first + last) // 2
        current_value = list[mid]
        if current_value == item:
            return mid
        if item > current_value:
            first = mid + 1
        else:
            last = mid - 1
    return None


list = [1, 3, 5, 7, 9]
print(binary_search(list, 5))

# To know how many steps a binary search will need to find a number in the worst case,
# it will be log2n
