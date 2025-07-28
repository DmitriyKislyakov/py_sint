def main(string: str) -> bool:
    # return string.isalpha()
    abc = 'qwertyuiopasdfghjklzxcvbnm'
    for s in string:
        if s.lower() not in abc:
            return False
    return True

if __name__ == '__main__':
    print(main('fadasdfisdaofAJSFKJFASDFJA'))