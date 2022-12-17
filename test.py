# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K, L):
    # write your code in Python 3.8.10
    for n in A:
        print(A[n])
    pass
def arr(A, K, L):
    S=[]
    D=[]
    temp = 0
    for n in range(len(A)-(K-1)):
        #print(n)
        for i in range(n,n + 2):
            #print(A[i])
            temp = temp + A[i]
            #print("/n")
            #temp =+ A[i]
        #print("/n")
        S.append(temp)
    temp=0
    for n in range(len(A)-(L-1)):
        #print(n)
        for i in range(n,n + 2):
            #print(A[i])
            temp = temp + A[i]
            #print("/n")
            #temp =+ A[i]
        #print("/n")
        D.append(temp)
    return max(S), max(D)
        #print(S)
    #for n in range(len(A)-(L+1)):
        #D.append(temp)
    #return max(S), max(D)
print(arr([4,5,6,8,10], 2, 3))