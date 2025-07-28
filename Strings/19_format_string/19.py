def main(name: str, age: int) -> str:
    # return f'Меня зовут {name}, мне {age} лет'
    return 'Меня зовут ' + name + ', мне ' + str(age) + ' лет'


if __name__ == '__main__':
    print(main('Dima', 34))
