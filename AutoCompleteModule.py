from AutoCompleteData import AutoCompleteData
import initial_function


#  -> list[AutoCompleteData]
def get_best_k_completions(prefix: str):
    result = []
    our_dictionary = initial_function.d
    found_count = 5
    for i in our_dictionary.items():
        if found_count == 0:
            break
        offset = i[0].find(prefix)
        if offset == -1:
            continue
        else:
            found_count = found_count - 1
            result.append(AutoCompleteData(i[0], i[1], offset, len(prefix) * 2))
    return result
