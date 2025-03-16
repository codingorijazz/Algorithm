N, M = map(int, input().split()) # N, M 을 입력받음.
A = [] # A를 빈 리스트로 초기화
B = [] # B를 빈 리스트로 초기화
for i in range(N): # N번 반복
    A.append(list(map(int, input().split()))) # A에 리스트로 입력받은 값을 추가
for i in range(N):
    B.append(list(map(int, input().split()))) # B에 리스트로 입력받은 값을 추가
for i in range(N):
    C = []
    for j in range(M): # M번 반복
        C.append(A[i][j]+B[i][j])
    print(*C) # 리스트 앞에 *을 달면 print를 예쁘게 할 수 있다.