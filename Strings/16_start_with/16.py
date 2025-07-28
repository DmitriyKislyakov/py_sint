def main(string: str, start='Hello') -> bool:
    # return string.startswith(start)
    for i, e in enumerate(start):
        if string[i] != e:
            return False
    return True


if __name__ == '__main__':
    print(main('Hello world!'))
