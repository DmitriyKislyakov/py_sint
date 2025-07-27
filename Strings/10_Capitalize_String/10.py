def main(string:str)->str:
    # return string.title()
    k = abs(ord('a') - ord('A'))
    lst = string.split()
    for ind, word in enumerate(lst):
        new_word = chr(ord(word[0]) - k) + word[1:]
        lst[ind] = new_word
    return ' '.join(lst)





if __name__ == '__main__':
    print(main('dsfdfa dfasf ads adf'))
