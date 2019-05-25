# exception

def calc(values):

    sum = None

    try:
        sum =  values[0] + values[1] + values[2]
    except IndexError as e:
        print('error ', e)
    except ValueError as e:
        print('error ', e)

    print(sum)

val = [12,-3] #index error list
calc(val)