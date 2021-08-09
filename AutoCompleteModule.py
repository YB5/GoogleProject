from AutoCompleteData import AutoCompleteData
import initial_function


def check_dif0(s, t):
    cost = 0
    dif = 0
    for i in range(len(s)):
        if dif > 1:
            break
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
    if dif > 1:
        return -6
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
            break
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
    if dif > 1:
        return -6
    return cost


#  -> list[AutoCompleteData]
def get_best_k_completions(prefix: str):
    result = []
    sub_d = initial_function.d_final[len(prefix.split())]
    scores = []
    print(sub_d)
    for i in sub_d:
        keys_to_find = list(i.keys())[0]
        values_to_find = list(i.values())[0]
        if len(keys_to_find) == len(prefix):
            sc = check_dif0(prefix, keys_to_find)
            if sc > -6:
                scores.append((sc, values_to_find))
        elif abs(len(keys_to_find) - len(prefix)) == 1:
            sc = check_dif1(prefix, keys_to_find)
            if sc > -6:
                scores.append((sc, values_to_find))
    sorted_scores = sorted(scores, key=lambda x: (x[0], x[1][0]))[:4]
    for r in sorted_scores:
        result.append(AutoCompleteData(r[1][0], r[1][1], r[1][2], r[0]))
    return result


