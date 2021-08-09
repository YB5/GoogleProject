from AutoCompleteData import AutoCompleteData
import initial_function


def check_dif0(s, t):
    cost = 0
    dif = 0
    for i in range(len(s)):
        if dif > 1:
            return -1
        if s[i] == t[i]:
            cost = cost + 2
            continue
        if s[i] != t[i]:
            if i == 0:
                cost = cost - 5
            elif i == 1:
                cost = cost - 4
            elif i == 2:
                cost = cost - 3
            elif i == 3:
                cost = cost - 2
            else:
                cost = cost - 1
            dif = dif + 1
    return cost


def check_dif1(s, t):
    if len(s) > len(t):
        temp = s
        s = t
        t = temp
    cost = 0
    dif = 0
    j = 0
    for i in range(len(s)):
        if dif > 1:
            return -1
        if s[i] == t[j]:
            cost = cost + 2
            j = j + 1
            continue
        if s[i] != t[j]:
            if i == 0:
                cost = cost - 10
            elif i == 1:
                cost = cost - 8
            elif i == 2:
                cost = cost - 6
            elif i == 3:
                cost = cost - 4
            else:
                cost = cost - 2
            j = j + 2
            dif = dif + 1
    return cost


#  -> list[AutoCompleteData]
def get_best_k_completions(prefix: str):
    result = []
    sub_d = initial_function.d[len(prefix.split())]
    scores = []
    for i in sub_d.items():
        if len(i[0]) == len(prefix):
            sc = check_dif0(prefix, i[0])
            if sc > 0:
                scores.append((sc, i[1]))
        else:
            sc = check_dif1(prefix, i[0])
            if sc > 0:
                scores.append((sc, i[1]))
    sorted_scores =  sorted(scores, key = lambda x: (x[0], x[1][0]))[:4]
    for r in sorted_scores:
        result.append(AutoCompleteData(r[1][0], r[1][1], r[1][2], r[0]))
    return result


