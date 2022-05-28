import time

n = 1000000

#에라토스테네스의 체 & set연산 - 다른사람 풀이 참고
start = time.time()
num = set(range(2, n + 1))

for i in range(2, n + 1):
    if i in num:
        num -= set(range(2 * i, n + 1, i))

print(len(num))
print(f'1 - 걸린 시간 : {time.time() - start}')

#1000000 기준 약 0.6초 소요

#sqrt(n) 이하 찾아낸 소수로 나누기
start = time.time()
if n <= 3:
    print(n - 1)

answer = 2
primes = [2, 3]

for nowNum in range(5, n + 1, 2):
    isNotPrime = False

    for nowPrime in primes:
        if nowPrime * nowPrime > nowNum:
            break

        if nowNum % nowPrime == 0:
            isNotPrime = True
            break

    if not isNotPrime:
        answer += 1
        primes.append(nowNum)

print(answer)
print(f'2 - 걸린 시간 : {time.time() - start}')

#1000000 기준 약 3초 소요