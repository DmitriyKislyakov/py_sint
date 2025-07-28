def main(d1: dict) -> dict:
    new_d = {}
    for k, v in d1.items():
        new_d[k] = v
    return new_d

d1= {1: 'abc', 2: 'cde', 3: 'def'}
if __name__ == '__main__':
    print(main(d1))


d2 = main(d1)

d2[2] = 'sadasdffs'
print(d1, d2, sep='\n')