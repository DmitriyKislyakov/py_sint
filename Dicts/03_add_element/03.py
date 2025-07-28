def main(*, d: dict) -> dict:
    d['job'] = 'developer'
    return d


if __name__ == '__main__':
    print(main(d={'name':'Dima', 'age':34}))
