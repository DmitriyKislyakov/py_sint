def main(string: str) -> bool:
    return len(string) == len(set(string))


if __name__ == '__main__':
    print(main('abcdefh'))