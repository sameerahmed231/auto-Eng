from Chapters.Ch2.add_number import add, is_even, is_positive, convert_to_number


def test_convert_string_to_number():
    number = convert_to_number('5')
    assert number == 5


def test_4_is_even():
    assert is_even(4)


def test_5_is_odd():
    assert is_even(5) is False


def test_adding_even_nums_return_even_numbers():
    number = add(2, 2)
    assert number == 4
    assert is_even(number)


def test_adding_negative_nums_return_negative_numbers():
    number = add(-1, -4)
    assert number == -5
    assert is_even(number) is False


def test_adding_odd_nums_return_even_numbers():
    number = add(3, 7)
    assert number == 10
    assert is_even(number)


def test_adding_even_and_odd_nums_return_positive_if_greater():
    number = add(3, -2)
    assert number == 1
    assert is_positive(number)


def test_string_input():
    output = add('sameer', 2)
    assert output == 'error: invalid number entered'
