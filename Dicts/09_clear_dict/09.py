def main(d: dict, n=1) -> dict:
    l = [k for k in d.keys()]
    for i in range(len(l)):
        d.pop(l[i])
    return d


d1 = {1:'dfs', 2:123, 3:'213123', 4:5}
if __name__ == '__main__':
    print(main(d1))
