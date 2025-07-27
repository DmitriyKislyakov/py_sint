def main(string:str, e='a')->int:
    count = 0
    for i in string:
        if i == e:
            count += 1
    return count


if __name__ == '__main__':
    print(main('sdfsafsfasdfd'))
