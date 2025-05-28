def text_lower_case(string):
    lowercase_string = string.lower()
    return lowercase_string


def seasons(user_input):
    season = text_lower_case(user_input)
    if season == 'winter':
        return'Snow'
    elif season == 'spring':
        return 'Flowers'
    elif season == 'summer':
        return 'Beach'
    elif season == 'fall' or season == 'autumn':
        return 'Leaves'
    else:
        return "I don't know the season"


def challenge_2():
    user_input = input('Enter a season ')
    print(seasons(user_input))


if __name__ == '__main__':
    challenge_2()