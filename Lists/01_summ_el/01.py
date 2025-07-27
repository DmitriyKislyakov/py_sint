def main(spisok: list) -> int:
    s = 0
    for e in spisok:
        s += e
    return s


if __name__ == '__main__':
    print(main([1, 21 , 35, 45]))
