def main(lst: list, length=3) -> list:
    # return [i for i in lst if len(i) > length]
    return list(filter(lambda x: len(x) > 3, lst))


if __name__ == '__main__':
    print(main(['apple', 'abc', 'orange', 'cde' 'apple', 'green']))
