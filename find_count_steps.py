from queue import Queue


def on_border(n_rows, n_cols, point):
    """
    Parameters:
    :n_rows (int): x-shape
    :n_cols (int): y-shape
    :point (tuple): point with x and y for check
    :return: bool value that tells whether a point is on the border
    """
    if point[0] == 0 or point[1] == 0 or point[0] == n_rows or point[1] == n_cols:
        return True
    else:
        return False


def possible_neighbours(point):
    """
    Parameters:
    :point (tuple): point with x and y for possible neighbours
    :return: list of nearby neighbors for point
    """
    x = point[0]
    y = point[1]
    return [(x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]


def count_steps(start, field):
    """
   Parameters:
   :start (tuple): start point with x and y 
   :field (list([])): field with waves
   :return: count steps
   """
    def on_field(p):
        if 0 <= p[0] <= rows - 1 and 0 <= p[1] <= cols - 1:
            return p


    def path2start(fin):
        n = possible_neighbours(fin)
        n = list(filter(on_field, n))
        for p in n:
            if field[fin[0]][fin[1]] - field[p[0]][p[1]] == 1:
                return True
        return False

    rows = len(field) - 1
    cols = len(field[0]) - 1
    steps = []
    for r in [0, rows]:
        for i in range(len(field[r])):
            if field[r][i] != 0 and path2start((r, i)):
                steps.append(field[r][i])

    for c in [0, cols]:
        for i in range(len(field)):
            if field[i][c] != 0 and path2start((i, c)):
                steps.append(field[i][c])
    if not steps:
        return 0
    steps.sort()
    return steps[0] - 1




def count_steps_to_exit(maze, start):
    """
    Parameters:
   :maze (list([])): the matrix with 0 and 1
   :start (tuple): start point with x and y
   :return: count steps
   """

    field = list(maze)
    rows = len(field)
    cols = len(field[0])

    if on_border(rows, cols, start):
        return 0

    def on_field(p):
        if 0 <= p[0] <= rows - 1 and 0 <= p[1] <= cols - 1 and not (p[0] == start[0] and p[1] == start[1]):
            return p

    q = Queue()
    nbs = possible_neighbours(start)

    for i in nbs:
        q.put(i)
    gen = 2;
    while not q.empty():
        curr_cells = []
        while not q.empty():
            curr_cells.append(q.get())
        # filter cells on field
        curr_cells = list(filter(on_field, curr_cells))

        for point in curr_cells:
            # push a wave
            if field[point[0]][point[1]] != 0 and field[point[0]][point[1]] == 1:
                field[point[0]][point[1]] = gen
                # put neighbours into queue
                for i in possible_neighbours((point[0], point[1])):
                    q.put(i)
        gen += 1

    return count_steps(start, field)
