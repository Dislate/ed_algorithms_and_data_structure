from collections import OrderedDict, defaultdict

if __name__ == "__main__":
    # Ordered dict
    od = OrderedDict()
    od['one'] = 1
    od['two'] = 2
    od2 = OrderedDict()
    od2['two'] = 2
    od2['one'] = 1
    print(od, od2, sep='\n')
    print(od == od2)  # False

    # default dict
    kvs = [('three', 3),
           ('four', 4),
           ('five', 5),
           ('six', 6),
           ]
    od.update(kvs)
    print(od)

    for k, v in od.items():
        print(k, v)
    '''
    one   1
    two   2
    three 3
    four  4
    five  5
    six   6
    '''

    od3 = OrderedDict(sorted(od.items(), key=lambda t: (4 * t[1]) - t[1] ** 2))
    print(od3.values())  # odict_values([6, 5, 4, 1, 3, 2])
