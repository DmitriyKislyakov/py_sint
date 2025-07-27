def main(string: str) -> str:
    while string[0] == ' ':
        string = string[1:]
    while string[-1] == ' ':
        string = string[: -1]
    return string


if __name__ == '__main__':
    print(main('   dsfsdfsdf fd gdf dfg fgdh dgf d    '))
