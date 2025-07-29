def main(string: str) -> dict:
    result = {}
    l = [w.lower().strip(',.!?:;-') for w in string.split()]
    for w in l:
        result[w] = result.setdefault(w, 0) + 1
    return result


text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit,\
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris\
 nisi ut aliquip ex ea commodo consequat.\
 Duis aute irure dolor in reprehenderit in voluptate velit esse cillum\
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.\
 dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,\
 sunt in culpa qui officia deserunt mollit anim id est laborum.'''
if __name__ == '__main__':
    print(main(text))
