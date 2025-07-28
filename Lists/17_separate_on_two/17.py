def main(lst: list) -> tuple:
    odd_list = [lst[i] for i in range(len(lst)) if i % 2 == 0]
    even_list = [lst[i] for i in range(len(lst)) if i % 2 == 1]
    return even_list, odd_list


if __name__ == '__main__':
    print(main(['apple', 'abc', 'orange', 'cde', 'apple', 'green']))
