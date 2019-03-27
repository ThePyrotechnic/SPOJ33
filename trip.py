# too lazy to write memoization for myself
from functools import lru_cache


class HashDict(dict):
    """
    Dictionaries can't be hashed, so let's wrap them 
    to make them work with memoization.
    """

    def __hash__(self):
        return id(self)


def lcs_table(alice, bob):
    # Fast enough
    lcs = {}
    for a in range(len(alice) + 1):
        lcs[a, 0] = 0
    for b in range(len(bob) + 1):
        lcs[0, b] = 0

    for a in range(1, len(alice) + 1):
        for b in range(1, len(bob) + 1):
            if alice[a - 1] == bob[b - 1]:
                lcs[a, b] = lcs[a - 1, b - 1] + 1
            else:
                lcs[a, b] = max(lcs[a - 1, b], lcs[a, b - 1])
    return HashDict(lcs)


@lru_cache()
def all_lcs_helper(table, alice, bob, a, b):
    # Definitely not fast enough
    if a == 0 or b == 0:
        return set()
    elif alice[a - 1] == bob[b - 1]:
<<<<<<< HEAD
        # Can use alice or bob
        result = all_lcs_helper(table, alice, bob, a - 1, b - 1)
        if result:
            return {sub_lcs + alice[a - 1] for sub_lcs in result}
=======
        lcs = set()
        res = all_lcs_helper(table, alice, bob, a - 1, b - 1)
        if len(res) > 0:
            for sub_lcs in res:
                lcs.add(f'{sub_lcs}{alice[a - 1]}')
>>>>>>> 0ddb465f765ca50ca20852c1bc55ea3ea9a4330f
        else:
            return {alice[a - 1]}
    else:
        lcs = set()
        if table[a, b - 1] >= table[a - 1, b]:
<<<<<<< HEAD
            result = all_lcs_helper(table, alice, bob, a, b - 1)
            lcs_2.update(result)
        if table[a - 1, b] >= table[a, b - 1]:
            result = all_lcs_helper(table, alice, bob, a - 1, b)
            lcs_2.update(result)
        return lcs_2
=======
            res = all_lcs_helper(table, alice, bob, a, b - 1)
            lcs.update(res)
        if table[a - 1, b] >= table[a, b - 1]:
            res = all_lcs_helper(table, alice, bob, a - 1, b)
            lcs.update(res)
        return lcs
>>>>>>> 0ddb465f765ca50ca20852c1bc55ea3ea9a4330f


def all_lcs(alice, bob):
    table = lcs_table(alice, bob)
    return all_lcs_helper(table, alice, bob, len(alice), len(bob))


def main():
    n = int(input())
    for a in range(n):
        alice = input()
        bob = input()
        lcs = sorted(all_lcs(alice, bob))
        [print(s) for s in lcs]

        if a != n - 1:
            print()


if __name__ == "__main__":
    main()
