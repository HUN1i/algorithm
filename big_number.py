n,m,k = map(int, input().split())
data = list(map(int,input().split()))

data.sort() # 데이터 정렬 
first = data[n-1] # 제일 큰 수 
second = data[n-2] # 2번째로 큰 수

result = 0
while True: # 무한반복 (어차피 m == 0 되면 break)
    for i in range(k): # k번 더하기
        if m == 0: # 만약 m이 0 이면 반복문 빠져나가기 
            break
        result += first
        m -= 1 # 연산 후 m 개수 줄이기 
    if m == 0:
        break
    result += second 
    m -= 1
    
print(result)
        
