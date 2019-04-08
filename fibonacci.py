def fibonacci(length):
    if type(length) is not int:
        raise TypeError("Length parameter should be of integer type")
    elif length < 1:
        raise TypeError("Sequence length can't be less then 1")
    else:
        if length == 1:
            sequence = [1]
        else:
            sequence = [1, 1]
            for i in range(2, length):
                sequence.append(sequence[i-1] + sequence[i-2])
        return sequence[-1]



