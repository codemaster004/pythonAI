main_block = (20, 50)
obstacles = [(0, 0, 5, 4)]

base_form = []


def create_form():
    for i in range(main_block[1]):  # X
        base_form.append([])
        for j in range(main_block[0]):  # Y
            if [obs for obs in obstacles if j in range(obs[0], obs[0] + obs[2]) and
                                            i in range(obs[1], obs[1] + obs[3])]:
                base_form[i].append(' ')
            else:
                base_form[i].append('\u2588')


def y_exist(j, y):
    if len(base_form[0]) >= j + y:
        return True
    else:
        return False


def x_exist(i, x):
    if len(base_form) >= i + x:
        return True
    else:
        return False


objects = (6, 4, "K")


def place_objects():
    for j in range(len(base_form)):  # Y
        for i in range(len(base_form[j])):  # X
            if base_form[j][i] == '\u2588' and y_exist(j, objects[1]) and x_exist(j, objects[0]):
                print(i, j)
                letter = objects[2]
                for y in range(objects[1]):
                    for x in range(objects[0]):
                        base_form[j + y][i + x] = letter

                return


def print_floor_plan():
    for i in range(len(base_form)):  # X
        for j in range(len(base_form[i])):  # Y
            print(base_form[i][j], end=' ')
        print('\n', end='')


create_form()
place_objects()
print_floor_plan()
