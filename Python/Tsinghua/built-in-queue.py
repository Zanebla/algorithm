from collections import deque

# q = deque([1, 2, 3], 5)
# q.append(1)
# print(q.popleft())

# q.appendleft(1)
# print(q.pop())


def tail(n):
    with open('test.txt', 'r') as f:
        q = deque(f, n)
        return q


for line in tail(5):
    print(line, end='')
