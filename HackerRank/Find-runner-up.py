if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    highest = 0
    second = 0
    for num in arr :
        if num > highest:
            second = highest
            highest = num
        if num > second and num < highest:
            second = num
    print(second)    
