N = int(input()) # 정수 입력 받기
result = 1  # 팩토리얼 결과 저장할 변수 (초기값은 1)

for i in range(1, N+1):  # 1부터 N까지 반복
    result *= i # result에 i를 계속 곱하기
    
print(result) # 최종 결과 출력