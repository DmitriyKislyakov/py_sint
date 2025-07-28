def main(d: dict) -> dict:
    values = sorted(d.values())
    new_d = {}
    for val in values:
        for k, v in d.items():
            if val == v:
                new_d[k] = v
                break
    return new_d


d1 = {1: 'abc', 2: 'cde', 3: 'def', 4: 'dsfasf0', 5: 'asdf0'}
if __name__ == '__main__':
    print(main(d1))
