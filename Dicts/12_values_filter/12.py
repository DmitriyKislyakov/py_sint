def main(d: dict) -> list:
    return [k for k, v in d.items() if v == 42]

d1 = {1: 'abc', 2: 'cde', 3: 'def', 4: 42, 5:'afsdfs', 'a': 42}
if __name__ == '__main__':
    print(main(d1))
