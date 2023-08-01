...
def reverse_ascending(numbers):
    result = []
    start = 0
    for n in range(len(numbers)):

        if numbers[n] <= numbers[n-1]:

            result += ((numbers[start:n][::-1]))
            start = n

    return result + numbers[start:][::-1]
    

