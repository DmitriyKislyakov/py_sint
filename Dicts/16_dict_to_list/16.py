def main(d: dict) -> list:
    return [(k, v) for k, v in d.items()]


d1 = {'a': 4, 'b': 17, 'c': 6, 'd':45}
if __name__ == '__main__':
    print(main(d1))
