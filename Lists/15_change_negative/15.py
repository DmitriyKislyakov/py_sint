def main(lst: list) -> list:
    for i in range(len(lst)):
        if lst[i] < 0:
            lst[i] = 0
    return lst


if __name__ == '__main__':
    print(main([1, 2, -3, 5, -7, 5, -8, -123, 34, 123]))
