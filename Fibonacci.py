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
        return sequence


def test_fibonacci():
    assert fibonacci(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert fibonacci(2) == [1, 1]
    assert fibonacci(1) == [1]


if __name__ == '__main__':
        print(fibonacci(99))
        test_fibonacci()


