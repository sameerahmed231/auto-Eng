def convert_to_number(string):
    return int(string)


def add(x, y):
    if isinstance(x, str) or isinstance(y, str):
        return 'error: invalid number entered'
    else:
        return x + y


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def is_positive(number):
    if number >= 0:
        return True
    else:
        return False


def challenge_1():
    input_1 = input('Enter a Number ')
    input_2 = input('Enter a Number ')
    num1 = convert_to_number(input_1)
    num2 = convert_to_number(input_2)
    total = add(num1, num2)
    print(total)


if __name__ == '__main__':
    challenge_1()