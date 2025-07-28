def main(lst: list) -> list:
    return [i for i in lst if i % 2 == 0]


if __name__ == '__main__':
    print(main([1, 2, 3, 5, 7, 5, 8, 123, 34, 123]))
