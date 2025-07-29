def main(d: dict) -> tuple:
    return list(d.keys()), list(d.values())


d1 = {1: 'abc', 2: 'cde', 3: 'def'}
if __name__ == '__main__':
    print(main(d1))
