def main(d1: dict, d2: dict) -> dict:
    # d1.update(d2)
    # return d1
    for k, v in d2.items():
        d1[k] = v
    return d1


d1= {1: 'abc', 2: 'cde', 3: 'def'}
d2 = {2: 'cde', 3: 'ghi', 4: 'rewrq'}

if __name__ == '__main__':
    print(main(d1, d2))
