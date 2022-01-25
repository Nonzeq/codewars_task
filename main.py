def direction(facing, turn):
    fast = [360,720,1080,-360,-720,-1080]
    facings = ['S', 'SW', 'W','NW', 'N', 'NE', 'E',
                  'SE',]
    if facing not in facings:
        raise ValueError('Введіть коректне направлення')
    elif turn < -1080 or turn > 1080:
        raise ValueError('Введіть число в даіпазоні від -1080 до 1080')
    elif turn % 45 != 0:
        raise ValueError('Введіть число кратне 45')
    if turn < 0:
        if turn in fast:
            return facing
        else:
            count = turn // 45
            index = facings.index(facing)
            if -8 > count > -16:
                count = count + 8
            elif count < -16:
                count = count + 16
            else:
                count = count
            if count + index > -8:
                data = count + index
                return facings[data]
            else:
                data = 7 - index
                out = count - data 
                return facings[out-1]

    else:
        if turn in fast:
            return facing
        else:
            count = turn // 45
            index = facings.index(facing)
            if 8 < count < 16:
                count = count - 8
            elif count > 16:
                count = count - 16
            else:
                count = count

            if count + index < 8:
                data = count + index
                return facings[data]
            else:
                data = 7 - index
                out = count - data 
                return facings[out-1]

v = direction('S', 1035)

print(v)