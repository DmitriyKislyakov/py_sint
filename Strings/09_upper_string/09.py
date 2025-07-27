def main(string:str)->str:
    k = abs(ord('a') - ord('A'))
    new_string = ''
    for i in string:
        new_string += chr(ord(i) - k)
    return new_string



if __name__ == '__main__':
    print(main('abcdefghilklmnopq'))
