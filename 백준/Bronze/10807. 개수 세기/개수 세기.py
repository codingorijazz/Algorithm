N = int(input()) # 숫자의 갯수
num = list(map(int, input().split())) # 숫자 리스트
v = int(input()) # 찾을 숫자

count = 0 # 등장 횟수를 저장할 변수

for n in num: # 리스트 num을 하나씩 순회
    if n == v: # 만약 현재 숫자가 v와 같다면
        count += 1

print(count)