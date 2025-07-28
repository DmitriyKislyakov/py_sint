import random

def main(length: int) -> str:
    password = ''
    abc = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    digit = '0123456789'
    simb = '@#$%^&*/-+'
    lst = [abc, digit, simb]
    for i in range(length):
        el_spis = random.choice(lst)
        rnd_el = random.choice(el_spis)
        password += rnd_el
    return password


if __name__ == '__main__':
    print(main(30))
