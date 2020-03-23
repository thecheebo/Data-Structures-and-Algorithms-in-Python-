def quick_sort(S):
    """Sort the elements of queue S using the quick-sort algorithm"""
    n = len(S)
    if n <2:
        return
    #divide
    p= S.last()
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()
    while not S.is_empty()
        if S.last() <p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue( ))
        else: # S.first() must equal pivot
            E.enqueue(S.dequeue( ))
        # conquer (with recursion)
    quick sort(L) # sort elements less than p
    quick sort(G) # sort elements greater than p
    # concatenate results
    while not L.is empty( ):
        S.enqueue(L.dequeue( ))
    while not E.is empty( ):
        S.enqueue(E.dequeue( ))
    while not G.is empty( ):
        S.enqueue(G.dequeue( ))
