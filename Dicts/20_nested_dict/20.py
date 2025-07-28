def main(d: dict, k:list) :
    dct = d
    for key in k:
        if key in dct:
            dct = dct[key]
        else:
            return False
    return dct



data = {
    'a': {
        'b': {
            'c': 42
        }
    }
}
keys = ['a', 'b', 'c']
if __name__ == '__main__':
    print(main(data, keys))
