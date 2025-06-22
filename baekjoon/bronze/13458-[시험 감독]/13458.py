#첫째 줄에 시험장의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
N = int(input())
#둘째 줄에는 각 시험장에 있는 응시자의 수 Ai (1 ≤ Ai ≤ 1,000,000)가 주어진다.
A = list(map(int, input().split()))
# B총 C부
B, C = map(int, input().split())

#각 시험장마다 응시생을 모두 감독하기 위해 필요한 감독관의 최소
cnt = len(A) #각반 B에대한 총감독 수 미리 더하기.

for i in range(len(A)):
    A[i] -= B #총 감독이 각 반에 관리 학생 제거
    if(A[i] > 0): #부감독이 나머지 관리
        cnt += (A[i] + C - 1) // C

        
            
        

print(cnt)

