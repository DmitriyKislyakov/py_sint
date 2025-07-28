def main(string: str) -> dict:
    d= {}
    for s in string:
        d[s] = d.setdefault(s, 0) + 1
    return d


text = 'hello world!'
if __name__ == '__main__':
    print(main(text))
