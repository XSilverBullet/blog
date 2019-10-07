# kmp字符串匹配算法
def patial_table(p):
    '''
    partial_table{'ABCDABD'}->{0,0,0,0,1,2,0}
    :param p:
    :return:
    '''
    prefix = set()
    postfix = set()

    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        ret.append(len((prefix & postfix or {''}).pop()))

    return ret


def gen_next(p):
    j, m = 0, len(p)

    next = [0] * m
    i = 1
    while i < m:
        if p[i] == p[j]:
            next[i] = j + 1
            j += 1
            i += 1
        elif j != 0:
            j = next[j - 1]
        else:
            next[i] = 0
            i += 1
    return next


def kmp_match(s, p):
    n, m = len(s), len(p)

    next = gen_next(p)

    i, j = 0, 0

    while i < n and j < m:
        if s[i] == p[j]:
            i += 1
            j += 1
        elif j != 0:
            j = next[j - 1]
        else:
            i += 1

    if j == m:
        return i - j
    else:
        return -1


print(patial_table('ABCDABD'))
print(gen_next('ABCDABD'))
print(kmp_match('abcxabcdabcdabcy', 'abcdabcy'))
