def main(d:dict) -> str:
    lst = []
    for k, v in d.items():
        lst.append(f'{k}:{v}')
    return ' '.join(lst)


d1 = {'a': 4, 'b': 17, 'c': 6, 'd':45}
if __name__ == '__main__':
    print(main(d1))
