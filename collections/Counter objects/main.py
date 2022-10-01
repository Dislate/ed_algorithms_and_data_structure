from collections import Counter

if __name__ == "__main__":
    c1 = Counter("anysequence")
    print(c1)  # Counter({'e': 3, 'n': 2, 'a': 1, 'y': 1, 's': 1, 'q': 1, 'u': 1, 'c': 1})
    c2 = Counter({
        'a': 1,
        "c": 1,
        "e": 3,
    })
    c3 = Counter(
        a=1,
        c=1,
        e=3,
    )
    print(c2)
    print(c3)

    ct = Counter()
    print(ct)  # empty Counter objects
    ct.update('abca')
    print(ct)  # Counter({'a': 2, 'b': 1, 'c': 1})
    ct.update({'a': 3})
    print(ct)  # Counter({'a': 5, 'b': 1, 'c': 1})

    for item in ct:
        print(item, ct[item])

    # Ordered dicts
    ct.update({
        'a': -3,
        'b': -2,
        'd': 3,
        'e': 2,
    })
    sorted(ct.elements())  # return a sorted list from the iterator
    print(ct)  # Counter({'d': 3, 'a': 2, 'e': 2, 'c': 1, 'b': -1})
    print(ct.most_common())
    ct.subtract({
        'a': 2,
    })
    print(ct)  # Counter({'d': 3, 'e': 2, 'c': 1, 'a': 0, 'b': -1})

