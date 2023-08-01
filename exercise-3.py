def remove_all_after(numbers, n):
    ...
    try:
        index = numbers.index(n)
        return numbers[:index+1]
    except ValueError:
        return numbers
