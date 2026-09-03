"""
You're given a stream of integers arriving one at a time. Implement a function that
maintains a sliding window of the last k integers and returns the current window's
sum after each new integer arrives.

Use deque for the window (efficient O(1) add/remove from both ends).
"""
from collections import deque


def sliding_window_sum(stream, k):
    totals, total = [], 0
    dq = deque()

    for num in stream:
        if len(dq) < k:
            dq.append(num)
            total += num
        else:
            total -= dq[0]
            dq.popleft()
            dq.append(num)
            total += num

        totals.append(total)

    return totals

stream = list(map(int, input("Enter values: ").split()))
k = int(input("Enter k: "))
print(sliding_window_sum(stream, k))


"""
Logged: 

collections | sliding_window_sum (deque-based) | Correct, first try, cold | 
Articulation: initial answer conflated running-total and deque optimizations into one, 
corrected with clear breakdown; follow-up question answered correctly and precisely | 
Referred: no | Insight: strong complexity reasoning once the two separate optimizations 
were disambiguated; good instinct on the follow-up showing real understanding, not 
memorized "deque = fast" without grasping why.
"""