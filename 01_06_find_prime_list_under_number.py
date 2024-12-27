input = 20

# 소수는 자기 자신과 1외에는 아무것도 나눌수 없음.
def find_prime_list_under_number(number):
    prime_list = []

    # 2 ~ 20 까지 찾아서 숫자들이 소수인지 판단.
    for n in range(2, number + 1): # 2 ~ number까지 숫자만큼 반복

        # for i in range(2, n): # 2 ~ n-1까지 i에 숫자 들어가는거 반복
        for i in prime_list: # n보다 작은 모든 소수에 대해서
            # if n % i == 0:  # n = 2, 3, 4, ... 20

            # N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다.
            if i * i <= n and n % i == 0:
                break       # n = 2 , i = x -> 아무일 일어나지 않고 prime_list 들어감.
        else:
            prime_list.append(n)
    return prime_list

result = find_prime_list_under_number(input)
print(result)