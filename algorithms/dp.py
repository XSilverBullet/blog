def lcs(a,b):

    n1 = len(a)
    n2 = len(b)

    dp = [[0 for i in range(n2+1)] for j in range(n1+1)]

    for i in range(1, n1+1):
        for j in range(1, n2+1):

            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n1][n2]

def longest_common_string(a, b):
    n1 = len(a)
    n2 = len(b)

    dp = [[0 for i in range(n2 + 1)] for j in range(n1 + 1)]

    max_ = -1
    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):

            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = 0
            max_ = max(dp[i][j], max_)

    return max_

def longest_increase_string(nums):


    n = len(nums)
    dp = [0 for i in range(n)]
    max_ = 0
    for i in range(n):
        tmp = 1
        for j in range(0, i):
            if nums[j] < nums[i]:
                tmp = max(tmp, 1+dp[j])
            dp[i] = tmp
        if max_ < tmp:
            max_ = tmp

    return max_

#最大连续子序列和
def max_xulie_sum(nums):

    n = len(nums)
    dp = [0 for i in range(n)] #记录以i为结尾的最大序列和

    dp[0] = nums[0]
    max_ = nums[0]
    for i in range(1, n):
        dp[i] = max(nums[i], dp[i-1]+nums[i])
        #print(dp[i])
        max_ = max(max_, dp[i])
    return max_

#最大连续子串乘积
def max_product(nums):
    l = len(nums)
    dpmax = [0 for _ in range(l)]
    dpmin = [0 for _ in range(l)]

    dpmax[0] = nums[0]
    dpmin[0] = nums[0]
    for i in range(1, l):
        dpmax[i] = max(nums[i], max(nums[i] * dpmax[i - 1], nums[i] * dpmin[i - 1]))
        dpmin[i] = min(nums[i], min(nums[i] * dpmax[i - 1], nums[i] * dpmin[i - 1]))

    return max(dpmax)


def minDistance(word1, word2):
    """
    :type word1: str
    :type word2: str
    :rtype: int
    """
    m = len(word1)
    n = len(word2)
    dp = [[0 for __ in range(m + 1)] for __ in range(n + 1)]
    for j in range(m + 1):
        dp[0][j] = j
    for i in range(n + 1):
        dp[i][0] = i

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if word1[j - 1] == word2[i - 1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i - 1][j], min(dp[i][j - 1] , dp[i - 1][j - 1]))+1
    return dp[n][m]
a = [0,2,4,5,0,7,10,1]
b = [1,2,6,0,7,2]

print(lcs("0245070101", "126072"))
print(longest_common_string("12378901", "2178910"))
print(longest_increase_string(a))
print(max_xulie_sum([-1,0,2,-4,5,0]))
print(max_product([-1,1,2,-4,5,0]))
