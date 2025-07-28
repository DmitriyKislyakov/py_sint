def main(lst: list) -> dict:
    new_dict = {}
    for i in lst:
        new_dict[i] = lst.count(i)
    return new_dict


if __name__ == '__main__':
    print(main(['apple', 'abc', 'orange', 'cde', 'apple', 'green', 'cde', 'dfgfsf']))
