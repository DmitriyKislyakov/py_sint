def main(l: list) -> dict:
    return {i[0]: i[1] for i in l}

l1 = [('a', 4), ('b', 17), ('c', 6), ('d', 45)]
if __name__ == '__main__':
    print(main(l1))
