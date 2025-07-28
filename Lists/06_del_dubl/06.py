def main(lst: list) -> list:
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


if __name__ == '__main__':
    print(main(['abc', 'cde', 'fgtg', 'abc', 123, 345, 123]))
