def main(lst: list) -> bool:
    for i in lst:
        if lst.count(i) > 1:
            return False
    return True


if __name__ == '__main__':
    print(main(['apple', 'abc', 'orange', 'cde', 'apple', 'green']))
