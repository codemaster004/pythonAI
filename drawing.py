from random import choice


rooms = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

max_attempts = 3

past_repetition = []

repetition = 0
done = False
while not done:
    repetition += 1
    routs_left = {
        'A': ['B', 'F', 'G'],
        'B': ['A', 'C', 'G'],
        'C': ['B', 'D', 'F'],
        'D': ['C', 'E', 'H'],
        'E': ['D', 'F', 'H'],
        'F': ['A', 'C', 'E'],
        'G': ['A', 'B', 'H'],
        'H': ['G', 'D', 'E']
    }
    attempted_routs = []
    for i in range(max_attempts):
        possible_rooms = [possible_room for possible_room in rooms if routs_left[possible_room]]
        current_room = choice(possible_rooms)
        while len(routs_left[current_room]) != 0:
            chosen_next_room = choice(routs_left[current_room])
            attempted_routs.append(f'{current_room}->{chosen_next_room}')

            routs_left[current_room].remove(chosen_next_room)
            routs_left[chosen_next_room].remove(current_room)

            current_room = chosen_next_room
        attempted_routs.append('end')

    print(attempted_routs)

    check_if_done = True
    for room in rooms:
        if check_if_done:
            if len(routs_left[room]) != 0:
                check_if_done = False
                print('false')
    done = check_if_done

    if repetition == 1000000:
        break

print('')
