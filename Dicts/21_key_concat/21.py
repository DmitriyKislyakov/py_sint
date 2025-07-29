def main(lst: list, k='id') -> dict:
    result = {}
    values_id = set()
    for d in lst:
        values_id.add(d.get(k))
    for i in values_id:
        result[i] = {}
    for d in lst:
        result[d[k]].update(d)
    return result



data = [
    {'id': 1, 'name': 'Alice', 'age': 25},
    {'id': 2, 'name': 'Bob', 'age': 30},
    {'id': 1, 'city': 'New York', 'age': 26}
]
if __name__ == '__main__':
    print(main(data))
