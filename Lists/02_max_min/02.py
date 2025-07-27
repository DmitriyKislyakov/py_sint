def main(spisok: list) -> tuple:
    min = max = spisok[0]
    for e in spisok:
        if e < min:
            min = e
        if e > max:
            max = e
    return min, max


if __name__ == '__main__':
    print(main([15, 21, 35, 4, 5, 26]))
