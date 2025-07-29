def main(n=5) -> dict:
    return {i: i**2 for i in range(1, n+1)}



if __name__ == '__main__':
    print(main())
