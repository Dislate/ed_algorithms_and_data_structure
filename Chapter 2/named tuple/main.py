from collections import namedtuple

if __name__ == "__main__":
    space = namedtuple("space", "x y z")
    s1 = space(x=2.0, y=4.0, z=10)
    print(s1.x * s1.y * s1.z)

    # With reserved keyword
    space2 = namedtuple('space2', 'x def z', rename=True)
    s2 = space2(3, 4, 5)
    print(s2._1)  # 4

    # With _replace method
    sl = [4, 5, 6]
    print(space._make(sl))  # space(x=4, y=5, z=6)

