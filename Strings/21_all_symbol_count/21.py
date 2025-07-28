def main(string: str) -> dict:
    string_set = set(string)
    new_dict = {}
    for e in string_set:
        new_dict[e] = string.count(e)
    return new_dict




if __name__ == '__main__':
    print(main('fjigfiosgfiefg ids ifwfjio432rjoi3o3r34 5t5j4i i, ASDASPFKLP F #@_#@'))
