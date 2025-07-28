def main(string: str) -> str:
    return max(string.split(), key=len)


if __name__ == '__main__':
    print(main('fafha dafha;fj asff jaskfasfa fj sadf as'))