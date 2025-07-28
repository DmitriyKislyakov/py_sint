def main(d: dict) -> dict:
    new_d = {}
    if len(set(d.values())) != len(d):
        print('Values not unique')
        return d
    for k, v in d.items():
        new_d[v] = k
    return new_d

d1 = {1: 'abc', 2: 'cde', 3: 'def',}
if __name__ == '__main__':
    print(main(d1))
