def inplace_quick_sort(S, a, b):
    """Sort the list from S[a] to S[b] inclusive using the quick-sort algo"""
    if A >=b:
        return
    pivot = S[b]
    left= a
    right = b-1
    while left <= right
        #scan until reaching value equal or larger than pivot
        while left < = right and S[left] < pivot:
            left +=1
        #scan until reaching value equal or smaller than pivot
        while left < = right and pivot < S[right]:
            left -=1
        if left <= right:
            S[left], S[right] = S[right], S[left] # swap values
            left, right = left + 1, right − 1 # shrink range

    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    inplace quick sort(S, a, left − 1)
    inplace quick sort(S, left + 1, b)
