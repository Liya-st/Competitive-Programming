if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    lists = []
    
    for p in range(x+1):
        for m in range (y+1):
            for o in range(z+1):
                if(p+m+o) != n:
                    lists.append([p,m,o])
    print(lists)
                    
    
