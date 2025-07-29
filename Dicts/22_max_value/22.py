def main(d: dict) -> str:
    max_value = max(d.values())
    for k in d.keys():
        if d.get(k) == max_value:
            return f'{k} is a key with max value {max_value}'




data = {'a':1, 'b': 54, 'c': 25, 'd':45, 'e':-73}
if __name__ == '__main__':
    print(main(data))
