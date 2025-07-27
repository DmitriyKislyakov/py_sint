def main(string: str) -> bool:
    return string == string[::-1]


if __name__ == '__main__':
    print(main('abccba'))
