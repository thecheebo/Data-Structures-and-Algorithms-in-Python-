def merge_sort(s):
    s_list_len = len(s)
    if s_list_len <2:
        return 
    #divide
    mid = s_list_len // 2
    firsthalfofS = s[0:mid]
    secondhalfofS = s[mid:s_list_len]
    #conquer with recursion)
    merge_sort(firsthalfofS)
    merge_sort(secondhalfofS)
    #mergge results
    merge(firsthalfofS, secondhalfofS, s)

def merge(S1,S2,S):
    """Merge two sorted Python lists and S2 into properly sized list S. """
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i]<S2[j]):
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1
 
