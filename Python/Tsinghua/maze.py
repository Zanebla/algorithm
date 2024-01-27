maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


dirs = [
    lambda x, y: (x, y-1),
    lambda x, y: (x+1, y),
    lambda x, y: (x, y+1),
    lambda x, y: (x-1, y)
]


def maze_path(x1, y1, x2, y2):
    stack = []
    stack.append((x1, y1))
    while (len(stack) > 0):
        curNode = stack[-1]
        # x, y four directions : x, y-1; x+1, y; x, y+1; x-1, y
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
