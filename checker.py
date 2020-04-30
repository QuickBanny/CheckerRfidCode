def get_true_codes(path_to_file: str = '') -> list:
    true_codes = []
    try:
        with open(path_to_file, 'r') as f:
            for cnt, line in enumerate(f):
                true_codes.append(line.replace('\n', ''))
    except:
        return true_codes
    return true_codes


def distance(a, b):
    "Calculates the Levenshtein distance between a and b."
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n
    current_column = range(n+1)# Keep current and previous column, not entire matrix
    for i in range(1, m+1):
        previous_column, current_column = current_column, [i]+[0]*n
        for j in range(1, n+1):
            add, delete, change = previous_column[j]+1, current_column[j-1]+1, previous_column[j-1]
            if a[j-1] != b[i-1]:
                change += 1
            current_column[j] = min(add, delete, change)
    return current_column[n]


def checker(code: str = '',
            path_to_codes_file: str = '',
            len_true_code: int = 11,
            n_changed: int = 3) -> str:
    true_code = ''
    true_code_list = get_true_codes(path_to_codes_file)
    if len(code) == len_true_code:
        return code
    for true_code in true_code_list:
        d = distance(code, true_code)
        if d <= n_changed and d != 0:
            return true_code
    return true_code
