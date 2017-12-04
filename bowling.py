


def get_result_when_not_strike(game, result, i, last):
    '''
    if score item is spare or else that is not strike, returns
    its value
    '''
    if game[i] == '/':

        result += 10 - last
        return result
    else:
        result += get_value(game[i])
        return result





def get_result_when_strike(game, result, frame, i):
    '''
    if score value is ten, and is not last frame,
    calculates the score including strike bonuses and so
    '''
    if frame < 10 and get_value(game[i]) == 10:
        result += get_value(game[i+1])
        if game[i] == 'X' or game[i] == 'x':
            if game[i+2] == '/':
                result += 10 - get_value(game[i+1])
                return result
            else:
                result += get_value(game[i+2])
                return result
        return result
    else:
        return result


def score(game):
    '''
    gets the results by calling subfunctions, and also, responsible for
    adjusting frame position, that is used in dubfunctions
    '''

    result = 0
    frame = 1
    in_first_half = True

    for i in range(len(game)):
        last = get_value(game[i-1])

        result = get_result_when_not_strike(game, result, i, last)

        result = get_result_when_strike(game, result, frame, i)

        if in_first_half is True:
            in_first_half = False
        else:
            frame += 1
            in_first_half = True

        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1

    return result


def get_value(char):
    '''
    calulates the value of the actual score item, if score item is invalid,
    raises error
    '''
    if char in "123456789":
        return int(char)
    elif char == 'X' or char == 'x' or char == '/':
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def main():
    print(score("5/11------------3/11"))
main()
