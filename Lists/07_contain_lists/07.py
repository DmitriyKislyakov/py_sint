def main(lst1: list, lst2: list) -> list:
    new_list = lst1
    for i in lst2:
        new_list.append(i)
    return new_list


if __name__ == '__main__':
    print(main(['abc', 'cde', 'fgtg', 'abc'], [123, 345, 123]))
