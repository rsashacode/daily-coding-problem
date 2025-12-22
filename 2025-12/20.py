def adds_up(l, k):
    seen = set()
    for n in l:
        if k - n in seen:
            return True
        seen.add(n)
    return False


if __name__ == '__main__':
    l = [10, 15, 3, 7]
    k = 17
    print(adds_up(l, k))