def f(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    p = [[None] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                p[i][j] = (i - 1, j - 1, s1[i - 1])
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    p[i][j] = (i - 1, j, '')
                else:
                    dp[i][j] = dp[i][j - 1]
                    p[i][j] = (i, j - 1, '')
                
        # for q in dp:
        #     print(q)
        # print(1111111111111111111111111)
    # print(dp)
    for i in dp:
        print(i)
    curr = p[n][m]
    result = ''
    while curr is not None:
        result += curr[2]
        curr = p[curr[0]][curr[1]]
    return dp[n][m], result[::-1]

if __name__ == "__main__":
    s1 = "abcaab"
    s2 = "acdaxxab"
    print(f(s1, s2))