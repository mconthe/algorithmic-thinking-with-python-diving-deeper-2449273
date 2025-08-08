# 2-Sum Interview Problem

def two_sum_problem(arr, target):
    sol = None
    n = len(arr)

    for idx1 in range(n):
        for idx2 in range(n):
            if idx1 != idx2:
                if arr[idx1] + arr[idx2] == target:
                    sol = (idx1, idx2)
                    
                    return sol
                

    return sol


assert two_sum_problem([1, 2, 3], 4) == (0, 2)
assert two_sum_problem([1234, 5678, 9012], 14690) == (1, 2)
assert two_sum_problem([2, 2, 3], 4) in [(0, 1), (1, 0)]
assert two_sum_problem([2, 2], 4) in [(0, 1), (1, 0)]
assert two_sum_problem([8, 7, 2, 5, 3, 1], 10) in [(0, 2), (2, 0), (1, 4), (4, 1)]
