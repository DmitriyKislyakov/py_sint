def main(string:str)->str:
    new_string = ''
    for i in string:
        if i == ' ':
            new_string += '_'
        else:
            new_string += i
    return new_string


if __name__ == '__main__':
    print(main('dsasfasf dfdgs fdgsd'))
