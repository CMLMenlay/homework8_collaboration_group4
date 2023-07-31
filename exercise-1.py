def replace_last(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        return [numbers[-1]] + numbers[:-1]
