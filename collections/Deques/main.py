import collections
from itertools import islice

if __name__ == "__main__":
    # Init deque
    dq = collections.deque('abc')

    # Adding methods to deque
    dq.append('d')  # adds the value 'd' to the right
    dq.appendleft('z')  # adds the value 'z' to the left
    dq.extend('efg')  # adds multiple items to the right
    dq.extendleft('yxw')  # adds multiple items to the left
    print(dq)  # deque(['w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])

    # Removes methods to deque
    dq.pop()  # returns and removes an item from the right // 'g'
    dq.popleft()  # returns and removes an item from the left // 'w'
    print(dq)  # deque(['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f'])

    # Other methods to deque
    dq.rotate(2)  # rotate all items 2 steps to the right
    print(dq)  # deque(['e', 'f', 'x', 'y', 'z', 'a', 'b', 'c', 'd'])
    dq.rotate(-2)  # rotate all items 2 steps to the left
    print(dq)  # deque(['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f'])

    # Deques have support slice
    dqslice = list(islice(dq, 3, 9))  # ['a', 'b', 'c', 'd', 'e', 'f']
    print(dqslice)

    # Circular buffer
    dq2 = collections.deque([], maxlen=3)
    for i in range(6):
        dq2.append(i)
        print(dq2)
    '''
    deque([0], maxlen=3)
    deque([0, 1], maxlen=3)
    deque([0, 1, 2], maxlen=3)
    deque([1, 2, 3], maxlen=3)
    deque([2, 3, 4], maxlen=3)
    deque([3, 4, 5], maxlen=3)
    '''