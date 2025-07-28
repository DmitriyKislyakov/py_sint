def main(lst: list, symb=',') -> str:
    # return ','.join(lst)
    string = ''
    for i in lst:
        string += i + symb
    return string[:-len(symb)]


if __name__ == '__main__':
    print(main(['afsdafasd', 'dsfasdfa', 'dsffdgdf']))
