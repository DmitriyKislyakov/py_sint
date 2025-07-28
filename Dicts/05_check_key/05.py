def main(d: dict, k) -> bool:
    return d.get(k) != None


if __name__ == '__main__':
    print(main(d={'name':'Dima', 'age':34}, k='abc'))
