def find_smallest(array):
    smallest = array[0]
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index


def selection_sort(array):
    ordered_list = []

    for i in range(len(array)):
        smallest_index = find_smallest(array)
        removed_item = array.pop(smallest_index)  # remove in the specified index and return the value removed
        ordered_list.append(removed_item)
    return ordered_list


list = [5, 3, 6, 2, 10]
print(selection_sort(list))
