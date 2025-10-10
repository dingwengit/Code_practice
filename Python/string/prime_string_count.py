# Given an integer cast as a string, count the number of ways to split the string into prime numbers. Since the result can be large, return the count modulo (109 + 7).
#
#     The digits must stay in the given order.
#     The entire string must be used.
#     Each resulting number:
#         must be within the range 2 to 106 inclusive.
#         must not have leading zeros.
#
#
#
# Example 1
#
# Input: s = "11375"
#
# Output: 3
#
# Explanation: [11, 37, 5], [11, 3, 7, 5], [113, 7, 5]
#
#
#
# Example 2
#
# Input: s = "3175"
#
# Output: 3
#
# Explanation:  [3, 17, 5], [31, 7, 5], [317, 5]
#
#
#
# Constraints
#
#     1 ≤ length of s ≤ 105
#     s does not have leading zeros.

def countPrimeStrings(s):
    MOD = 10**9 + 7
    MAX = 10**6
    L = len(s)
    prime = [True for _ in range(MAX + 3)]
    prime[0] = prime[1] = False
    i = 2
    while i * i <= MAX:
        print(f"prime[i]: i={i}, {prime[i]}")
        if prime[i]:
            for j in range(i * i, MAX + 1, i):
                prime[j] = False
                print(f"prime[j]: j={j}, {prime[j]}")
        i += 1

    dp = [0 for _ in range(L + 1)]
    dp[0] = 1
    for l in range(1, L + 1):
        for j in range(l - 1, max(-1, l - 7), -1):
            print(f"s[{j}:{l}], {s[j:l]}")
            num = int(s[j:l])
            if num > 10 ** 2:
                break
            if s[j] == '0':
                continue
            print(f"num={num}, prime[num]={prime[num]}")
            if prime[num]:
                dp[l] = (dp[l] + dp[j]) % MOD
        print(f"l={l}, dp={dp}")
    print(dp)
    return dp[-1]

def countPrimeStrings_method2(s):
    MAX = 10 ** 6
    prime = [True] * (MAX+1)
    prime[0] = prime[1] = False
    i = 2
    while (i*i  <= MAX):
        if prime[i]:
            for j in range(i*i, MAX + 1, i):
                prime[j] = False
        i += 1
    res = []
    countPrimeStrings_method2_recur(s, prime, 0, res)

cnt = 0
def countPrimeStrings_method2_recur(s, prime, idx, res):
    global cnt
    if idx >= len(s) and len(res) > 0:
        cnt += 1
        print(res)
        return
    for i in range(1,7):
        if idx+i > len(s):
            break
        num = int(s[idx:idx+i])
        if s[idx] != '0' and prime[num]:
            res.append(num)
            countPrimeStrings_method2_recur(s, prime, idx+i, res)
            del res[-1]

# print(countPrimeStrings("11375"))
countPrimeStrings_method2("11375")
print(f"cnt={cnt}")