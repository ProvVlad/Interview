
def is_even(value):
    """ Function return True, if value is even."""
    
    return bin(value)[-1] == '0'


def test_is_even():
    """Unittests for function 'is_even'."""

    number = -1
    result = is_even(number)
    assert result == False, 'Wrong answer by nuber: {}'.format(number)
    number = -2
    result = is_even(number)
    assert result == True, 'Wrong answer by nuber: {}'.format(number)
    number = 0
    result = is_even(number)
    assert result == True, 'Wrong answer by nuber: {}'.format(number)
    number = 1
    result = is_even(number)
    assert result == False, 'Wrong answer by nuber: {}'.format(number)
    number = 2
    result = is_even(number)
    assert result == True, 'Wrong answer by nuber: {}'.format(number)
    print('All tests passed')


if __name__ == '__main__':
    test_is_even()