##program check even numbers
##from collections import Counter
from collections import  Counter
def solution(S):
    freq = Counter(S)
    deletions = sum(count% 2 for count in freq.values())
    return deletions
