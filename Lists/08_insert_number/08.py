def main(lst: list) -> list:
    # lst.insert(3, 42)
    # return lst
    lst1 = lst[:3]
    lst2 = lst[3:]
    lst1.append(42)
    lst1.extend(lst2)
    return lst1


if __name__ == '__main__':
    print(main([1, 2, 3, 5, 6]))