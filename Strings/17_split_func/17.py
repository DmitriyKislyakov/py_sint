def main(string: str) -> list:
    # return string.split()
    lst = []
    space_count = string.count(' ')
    for i in range(space_count):
        lst.append(string[:string.index(' ')])
        string = string[string.index(' ') + 1:]
    lst.append(string)
    return lst



if __name__ == '__main__':
    print(main('dasd a asd a fsd fsdf s'))
