def main(string: str)-> str:
    if len(string) > 4:
        return string[2:6]
    return 'строка меньше 5 символов'


if __name__ == '__main__':
    print(main('abcde'))
