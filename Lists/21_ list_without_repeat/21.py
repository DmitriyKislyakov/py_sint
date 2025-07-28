def main(lst: list) -> list:
    return [i for i in lst if lst.count(i) < 2]


if __name__ == '__main__':
    print(main(['apple', 'abc', 'orange', 'cde', 'apple', 'green', 'cde', 'dfgfsf']))
