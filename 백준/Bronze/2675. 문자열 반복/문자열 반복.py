for _ in range(int(input())):
    A, B = input().split()
    print(''.join(char * int(A) for char in B))