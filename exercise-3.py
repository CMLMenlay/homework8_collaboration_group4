def remove_all_after(numbers, n):
    ...
    try:
        index = numbers.index(n)
        del numbers[index+1:]
    except ValueError:
        pass


