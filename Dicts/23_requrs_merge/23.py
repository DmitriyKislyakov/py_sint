def main(d1: dict, d2: dict) -> dict:
    result = d1.copy()
    for k, v in d2.items():
        if (k in result and type(result[k]) is dict) and (type(v) is dict):
            result[k] = main(result[k], d2[k])
        else:
            result[k] = v
    return result


dict1 = {'a': 1, 'b': {'x': 10, 'y': 20}}
dict2 = {'b': {'y': 30, 'z': 40}, 'c': 3}
if __name__ == '__main__':
    print(main(dict1, dict2))
