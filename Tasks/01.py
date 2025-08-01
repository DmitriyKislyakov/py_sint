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
print(sum_first_half(lst))

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

print(update_dict(dct1, dct2))
