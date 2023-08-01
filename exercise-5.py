...
def reverse_ascending(numbers):
    result = []
    start = 0

    for n in range(len(numbers)):

        if numbers[n] <= numbers[n-1]:

            result += ((numbers[start:n][::-1]))
            start = n

    return result + numbers[start:][::-1]


# assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
# assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [
#     10,
#     7,
#     5,
#     4,
#     8,
#     7,
#     2,
#     3,
#     1,
# ]
# assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
# assert list(reverse_ascending([])) == []
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14