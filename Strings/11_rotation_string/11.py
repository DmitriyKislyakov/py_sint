def main(string: str) -> str:
    k = ord('a') - ord('A')
    new_str = ''
    for i in range(len(string)):
        if i % 2 == 0:
            new_str += chr(ord(string[i]) - k)
        else:
            new_str += string[i]
    return new_str


if __name__ == '__main__':
    print(main('abcdefghi'))
