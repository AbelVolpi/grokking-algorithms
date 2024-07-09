def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)


def sum(list):
    if list == []:
        return 0
    else:
        return list[0] + sum(list[1:])


def count(list):
    if list == []:
        return 0
    else:
        return 1 + count(list[1:])


def find_max(list):
    if len(list) == 1:
        return list[0]
    else:
        max_of_rest = find_max(list[1:])
        return max_of_rest if max_of_rest > list[0] else list[0]


print(factorial(5))
print(sum([1, 2, 3, 4, 5]))
print(count([1, 2, 3, 4, 5]))
print(find_max([1, 2, 60, 4]))
