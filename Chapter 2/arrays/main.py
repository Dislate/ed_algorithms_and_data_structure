import array
import sys

if __name__ == '__main__':
    ba = array.array('i', range(10 ** 6))

    bl = list(range(10 ** 6))
    print(100 * sys.getsizeof(ba) / sys.getsizeof(bl))
    print(sys.getsizeof(ba), sys.getsizeof(bl))