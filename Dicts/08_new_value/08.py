def main(d: dict, n=1) -> dict:
    for k, v in d.items():
        if type(v) is int:
            d[k] = v + n
    return d

d1 = {1:'dfs', 2:123, 3:'213123', 4:5}
if __name__ == '__main__':
    print(main(d1))
