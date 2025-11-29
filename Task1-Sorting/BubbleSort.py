# Bubble Sort
# aka comparison sort

def swap(A,a,b):
    t=A[a]
    A[a]=A[b]
    A[b]=t

def bubblesort(A):
    n=len(A)
    for j in range(n-1):
        swapped=False
        for i in range(n-1):
            if A[i]>A[i+1]:
                swap(A,i,i+1)
                # print(A)
                swapped=True
        if swapped==False:
            break
    return A

#print(bubblesort([5,3,100,4,7,1]))


