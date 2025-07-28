def main(lst1: list, lst2: list) -> list:
    new_list = []
    for i in lst1:
        if i in lst2:
            new_list.append(i)
    return new_list


if __name__ == '__main__':
    print(main(['apple', 'abc', 'orange', 'cde'],  ['apple', 'green', 'cde', 'dfgfsf']))
