def main(lst: list) -> list:
    return [i**2 for i in lst]


if __name__ == '__main__':
    print(main([1, 2, 3, 5, 7, 5, 8, 123, 34, 123]))
