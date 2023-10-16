import numpy as np

# f=open('print.txt', 'w')

def win(position, ox=1):
    position = np.copy(position)
    if ox:
        position[position<0] = 0
    else:
        position[position<0] = 1
        position = 1 - position
    v = np.any(np.all(position, axis=0))
    h = np.any(np.all(position, axis=1))
    c1 = np.all(position.diagonal())
    c2 = np.all(np.flip(position, axis=1).diagonal())
    return v or h or c1 or c2

def o_turns(position):
    position = np.copy(position)
    nextchess = (position < 0).flatten()
    results = []
    for n in range(9):
        if not nextchess[n]:
            continue
        position_next = np.copy(position)
        position_next[n//3, n%3] = 1
        if win(position_next):
            # print(position_next, 'o', file=f) #
            results.append(True)
            continue
        results.append(x_turns(position_next))
    return any(results)


def x_turns(position):
    position = np.copy(position)
    nextchess = (position < 0).flatten()
    if not np.any(nextchess):
        # print(position, 'x_full', file=f) #
        return False
    results = []
    for n in range(9):
        if not nextchess[n]:
            continue
        position_next = np.copy(position)
        position_next[n//3, n%3] = 0
        if win(position_next, ox=0):
            # print(position_next, 'x', file=f) #
            results.append(False)
            continue
        results.append(o_turns(position_next))
    return all(results)


init_position = np.ones((3, 3), dtype='int')*-1
print(init_position)
print('First person must win:', o_turns(init_position))

# f.close()