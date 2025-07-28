def main(*, dct: dict, k):
    return dct.get(k)


if __name__ == '__main__':
    print(main(dct={1:'asdas', 2:'dsafdds'}, k=4))
