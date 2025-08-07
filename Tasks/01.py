import random


def first_n(n1: int, n2:int):
    return str(n1)[0] == str(n2)[0]

def str_to_list(string:str) -> list:
    return list(string)

def dict_to_data(d:dict) -> str:
    return '-'.join(d.values())

data_dict = {
	'year' : '2025',
	'month': '12',
	'day'  : '31',
}

def sum_first_half(l:list) -> int:
    return sum(l[:int(len(l)/2)])

lst = [1, 2, 3, 4, 5, 6]
# print(sum_first_half(lst))

def update_dict(d1: dict, d2: dict) -> dict:
    new_d = d1.copy()
    new_d.update(d2)
    return new_d

dct1 = {
	'a': 1,
	'b': 2,
}
dct2 = {
	'c': 3,
	'd': 4,
}

# print(update_dict(dct1, dct2))

def nod(a:int, b:int) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def low_o_d(a, b):
    n = 2
    while n > 1:
        if a % n == 0 and b% n == 0:
            return n
        n+= 1



def reduction_fraction(fract: str) -> str:
    result = [fract]
    a, b = map(lambda x: int(x), fract.split('/'))
    while nod(a, b) != 1:
        result.append(f'{int(a/low_o_d(a, b))}/{int(b/low_o_d(a, b))}')
        n = low_o_d(a, b)
        a /= n
        b /= n
    return '='.join(result)


# print(reduction_fraction('12/16'))

def plural(word: str) -> str:
    exeptions = {'man': 'men', }
    vovels = ['a', 'q', 'e', 'y', 'u', 'o', 'a']
    if word in exeptions:
        return exeptions[word]
    if word[-1] == 'o':
        return word + 'es'
    if word[-1] == 'f':
        return word[:-1] + 'ves'
    if word[-2:] == 'fe':
        return word[:-2] + 'ves'
    if word[-1] == 'y':
        if word[-2] in vovels:
            return word + 's'
        return word[:-1] + 'ies'
    if word[-1] in ['s', 'x', 'z'] or word[-2:] in ['ss', 'sh', 'ch']:
        return word + 'es'
    return word + 's'

# print(plural('man'))

def words_list(text: str) -> list:
   return [word.strip(' .,-!?/') for word in text.split() if word.strip(' .,-!?/') != '']

print(* words_list('aaa bbb, ccc. Xxx - eee bbb, kkk!'))

def multi(a: int, b: int):
    result = [str(a).rjust(len(str(a * b)), ' '),
              str(b).rjust(len(str(a * b)), ' '),
              '-'*len(str(a * b))]

    for i in range(len(str(b))):
        result.append(str(a * int(str(b)[::-1][i])).rjust(len(str(a * b)) - i, ' '))
    result.append('-'*len(str(a * b)))
    result.append(a * b)
    for i in result:
        print(i)

multi(321654,  1532423)

def new_row(matrix: list) -> list:
    res = matrix.copy()
    res.append([random.randint(1, 100) for i in range(len(matrix[0]))])
    return res


m = [
	[11, 12, 13],
	[21, 22, 23],
	[31, 32, 33],
]
# print(new_row(m), m, sep='\n')

def squard_roots(a:int, b:int, c:int) -> tuple:
    d = b**2 - 4 * a * c
    if d > 0:
        return (-b + d**0.5)/(2*a), (-b - d**0.5)/(2*a)
    if d == 0:
        return -b / (2 * a),
    return (None,)

# print(squard_roots(4, 5, 1))

def random_word(text: str):
    n_t = text.split()
    random.shuffle(n_t)
    return ' '.join(n_t)

random_word('dfsdfs fa sa f asfggfdg dfgsg df ')


def zero_column(lst: list, n: int):
    for r in range(len(lst)):
        lst[r][n] = 0
    return lst

l = [
	[11, 12, 13, 14, 15],
	[21, 22, 23, 24, 25],
	[31, 32, 33, 34, 35],
	[41, 42, 43, 44, 45],
	[51, 52, 53, 54, 55],
]

print(zero_column(l, 3))

def new_equation():
    while True:
        a, b, c = random.randint(1, 100), random.randint(1, 100), random.randint(1, 100)
        if (b**2 - 4*a*c) >0:
            return f'{a}x**2 + {b}x + {c}'

print(new_equation())
