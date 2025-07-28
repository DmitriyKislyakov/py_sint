def main(lst: list, simb=5) -> list:
    while simb in lst:
        lst.remove(simb)
    return lst


if __name__ == '__main__':
    print(main([1, 2, 3, 5, 7, 5, 8, 123, 34, 123]))
