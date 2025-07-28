def main(d: dict) -> dict:
    d.pop('age')
    return d


if __name__ == '__main__':
    print(main(d={'name':'Dima', 'age':34}))
