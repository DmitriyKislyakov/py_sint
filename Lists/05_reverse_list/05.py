def main(lst: list) -> list:
    new_lst = []
    for i in lst:
        new_lst.insert(0, i)
    return new_lst


if __name__ == '__main__':
    print(main(['sadadsfsa', 'fgfaadg', 123654, 464]))
