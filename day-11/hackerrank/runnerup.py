if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    b=max(arr)
    while max(arr)==b:
        arr.remove(max(arr))
    print(max(arr))

