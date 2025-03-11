import sys

data = sys.stdin.read().splitlines()
for line in data:
    a, b = map(int, line.split())
    print(a + b)










# import sys

# for i in sys.stdin:
#     A, B = map(int,i.split())
#     print(A+B)






# while True:
#     try:
#         A,B = map(int,input().split())
#         print(A+B)
#     except:
#         break"