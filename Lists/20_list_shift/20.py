def main(lst: list, n=1) -> list:
    new_list = []
    length = len(lst)
    new_list.extend(lst[length - n: ])
    new_list.extend(lst[:length - n])
    return new_list


if __name__ == '__main__':
    print(main([1, 2, 3]))
