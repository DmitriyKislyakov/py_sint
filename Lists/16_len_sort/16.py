def main(lst: list) -> list:
    return sorted(lst, key=len)


if __name__ == '__main__':
    print(main(['apple', 'abc', 'orange', 'cde', 'apple', 'green']))
