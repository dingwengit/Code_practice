'''
Given a string of length n containing digits [0-9], count the number of ways to split the string into prime numbers.
The digits must stay in the given order, and the entire string must be used.
Each resulting number must be within the range 2 to 10~6 inclusive and must not have leading zeros. Since the result can be large, return the count modulo (109 + 7).
Note: The initial string has no leading zeros.
Example
s = "11375"
This string can be split into primes 3 different ways:
[11, 37, 5], [11,3, 7, 5], [113, 7, 5].
'''

def num_prime_strings(str):
    if not str:
        return 0
    last_int = int(str[len(str)-1])
    if last_int % 2 == 0:
        return 0
    MAX = 10 ** 6 + 3
    prime = [True for _ in range(MAX)]
    prime[0] = prime[1] = prime[2] = False
    i = 2
    while (i * i <= MAX):
        for j in range(i * i, MAX+1, i):
            if prime[j]:
                prime[j] = False
        i += 1
    res = []
    for l in range(1, len(str)+1):
        check_prime_strings(str, l, 0, [], res, prime)
    print(res)
    return len(res)


def check_prime_strings(str, l, st_idx, cur_res, res, prime):
    s = str[st_idx:st_idx+l]
    # print(f"s={s}")
    if s[0] == '0':
        return
    if l >= 7 or int(s) <= 2:
        return
    if st_idx + l > len(str):
        return
    if prime[int(s)]:
        cur_res.append(s)
        # print(f"cur_res={cur_res}, res={res}, st_idx={st_idx}, l={l}")
        if st_idx + l >= len(str):
            # print(f"adding cur_res={cur_res}, res={res}")
            res.append(cur_res.copy())
            return
        for new_len in range(1, len(str)-l-st_idx+1):
            n = len(cur_res)
            # print(f"cur_res={cur_res}, new_len={new_len}, st_idx={st_idx}, l={l}")
            check_prime_strings(str, new_len, st_idx+l, cur_res, res, prime)
            m = len(cur_res)
            for _ in range(n, m):
                del cur_res[-1]


str = "11375"
# print(num_prime_strings(str))

# other solution - not common, using dp array
def countPrimeStrings(s):
    MAX = 10**6
    res = dict()
    L = len(s)
    prime = [True for _ in range(MAX + 3)]
    prime[0] = prime[1] = False
    i = 2
    while i * i <= MAX:
        if prime[i]:
            for j in range(i * i, MAX + 1, i):
                prime[j] = False
        i += 1
    dp = [0 for _ in range(L + 1)]
    dp[0] = 1
    for l in range(1, L + 1):
        for j in range(l - 1, max(-1, l - 7), -1):
            # print(f"j={j}, l={l}, s[j:l]={s[j:l]}")
            num = int(s[j:l])
            if num > 10 ** 6:
                break
            if s[j] == '0':
                continue
            if prime[num]:
                if dp[j] > 0:
                    if j == 0:
                        if l in res:
                            res[l].append([num])
                        else:
                            res[l] = [[num]]
                    else:
                        for item in res[j]:
                            new_item = item.copy()
                            new_item.append(num)
                            if l in res:
                                res[l].append(new_item)
                            else:
                                res[l] = [new_item]
                dp[l] = dp[l] + dp[j]
                # print(f"dp={dp}, res={res}")
    return dp[-1], res[len(str)]

str = "11375"
print(countPrimeStrings(str))
