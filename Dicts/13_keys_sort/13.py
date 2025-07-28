def main(d: dict) -> dict:
    keys = sorted(d)
    new_d = {}
    for k in keys:
        new_d[k] = d[k]
    return new_d



d1 = {'abc': 1, 'cde': 2, 'def': 3, 'dsfasf0': 4, 'asdf0': 5}
if __name__ == '__main__':
    print(main(d1))
