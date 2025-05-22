# Homework 03: randomized quick sort

import random

def make_random_list(length=20):
    """ ritorna una lista lunga length di elementi random con valori tra 0 e length """
    return [ random.randint(0,length) for _ in range(length) ]

# randomized quick sort
def randomized_partition(A=[],p=0,r=None):
    if r is None: r=len(A)-1
    i = random.randint(p,r)
    A[i],A[r] = A[r],A[i]
    return partition(A,p,r)

def partition(A=[],p=0,r=None):
    """
    partizioniamo l'array, partition e' un po' come il merge del merge sort
    A array
    p p-artenza
    r r-ivo
    """
    if r is None: r=len(A)-1  
    # x, pivot, ultimo elemento, per convenzione
    x = A[r]
    # indice piu' alto della parte bassa
    i = p-1 
    # processa ogni elemento dell'array tranne il pivot
    for j in range(p,r):
        if A[j] <= x:
            i=i+1
            # scambio A[i] con A[j]
            # nella prima iterazione non ha senso perche' inizialmente questo sara' lo stesso elemento
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def randomized_quick_sort(A=[],p=0,r=None):
    """
    A array
    p partenza
    r r-ivo
    """
    if r is None: r=len(A)-1
    if p<r:
        # teniamo q indice di arrivo del pivot
        q = randomized_partition(A,p,r)
        randomized_quick_sort(A,p,q-1)
        randomized_quick_sort(A,q+1,r)

def main(A=[],p=0,r=None):
    return randomized_quick_sort(A,p,r)
