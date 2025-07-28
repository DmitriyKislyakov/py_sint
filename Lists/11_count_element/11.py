def main(lst: list, element='apple') -> int:
    # return lst.count(element)
    count = 0
    for i in lst:
        if i == element:
            count += 1
    return count


if __name__ == '__main__':
    print(main(['apple', 'orange', 'apple', 'green', 'apple', 'apple']))
