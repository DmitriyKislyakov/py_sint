def main(string: str) -> bool:
    # return string.isdigit()

    digit = '0123456789'
    for s in string:
        if s not in digit:
            return False
    return True


if __name__ == '__main__':
    print(main('213124324 sdfgsdfgs '))