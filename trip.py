def lcs_table(alice, bob):
    # Fast enough
    lcs = dict()

    for a in range(len(alice) + 1):
        for b in range(len(bob) + 1):
            if a == 0 or b == 0:
                lcs[a, b] = 0
            elif alice[a - 1] == bob[b - 1]:
                lcs[a, b] = lcs[a - 1, b - 1] + 1
            else:
                lcs[a, b] = max(lcs[a - 1, b], lcs[a, b - 1])
    return lcs


def all_lcs_helper(table, alice, bob, a, b):
    # Definitely not fast enough
    if a == 0 or b == 0:
        return set()
    elif alice[a - 1] == bob[b - 1]:
        lcs = set()
        res = all_lcs_helper(table, alice, bob, a - 1, b - 1)
        if len(res) > 0:
            for sub_lcs in res:
                lcs.add(f'{sub_lcs}{alice[a - 1]}')
        else:
            lcs.add(alice[a - 1])
        return lcs
    else:
        lcs = set()
        if table[a, b - 1] >= table[a - 1, b]:
            res = all_lcs_helper(table, alice, bob, a, b - 1)
            lcs.update(res)
        if table[a - 1, b] >= table[a, b - 1]:
            res = all_lcs_helper(table, alice, bob, a - 1, b)
            lcs.update(res)
        return lcs


def all_lcs(alice, bob):
    return all_lcs_helper(lcs_table(alice, bob), alice, bob, len(alice), len(bob))


def main():
    n = int(input())
    for a in range(n):
        alice = input()
        bob = input()
        lcs = sorted(all_lcs(alice, bob))
        [print(s) for s in lcs]

        if a != n - 1:
            print()


if __name__ == '__main__':
    main()
