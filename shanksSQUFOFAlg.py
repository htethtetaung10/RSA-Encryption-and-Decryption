from math import floor
from math import sqrt


def shanksSQUFOF(n):
    multipliers = [1, 3, 5, 7, 11, 3 * 5, 3 * 7, 3 * 11, 3 * 13, 3 * 17, 3 * 19, 3 * 23, 3 * 29, 5 * 7, 5 * 11, 7 * 11, 3 * 5 * 7, 3 * 5 * 11, 3 * 7 * 11,5 * 7 * 11, 3 * 5 * 7 * 11]

    for i in multipliers:
        factor =SQUFOF(n, i)
        # print(factor)
        if factor != 0:
            return factor

def SQUFOF(N, k):
    factor = 0
    P0 = floor(sqrt(k * N))
    sqrtKN = P0
    pPrev = P0
    Q0 = 1
    qPrev = Q0
    Q1 = (k * N) - (P0 ** 2)
    Q = Q1
    L = 2 * sqrt( 2* sqrtKN)
    B = 3 * L
    i = 1
        
    # print("P0:", P0)
    # print("Q0:", Q0)
    # print("Q1:", Q1)
    # print()

    qNext = 2
    while (i < B and isPerfectSquare(int(qNext)) == False):           
        # print("pPrev:", pPrev)
        # print("qPrev:", qPrev)
        # print("Q:", Q)
            
        b = floor((sqrtKN + pPrev) / Q)
        P = (b * Q) - pPrev
        qNext = qPrev + b * (pPrev - P)
        pPrev = P
        qPrev = Q
        Q = qNext
        i = i + 1

        # print("P:", P)
        # print("qNext:", qNext)
        # print("b", b)
        # print()
            
        b = floor((sqrtKN + P0) / Q1)
        P1 = (b * Q1) - P0
        Q2 = Q0 + b * (P0 - P1)
        
    sqrtQNext = sqrt(qNext)
    b0 = floor((P0 - P) / sqrtQNext)
    P0 = (b0 * sqrtQNext) + P
    pPrev = P0
    pOld = 0
    Q0 = sqrtQNext
    qPrev = Q0
    Q1 = floor(((k * N) - P0 ** 2) / Q0)
    Q = Q1
    revereCycle = i
    j = 1
    
    while (P != pOld and j < B):
        pOld = pPrev
        b = floor((P0 + P) / Q)
        pPrev = P
        P = (b * Q) - P
        qNext = qPrev + (b * (pPrev - P))

        qPrev = Q
        Q = qNext
        j = j + 1
        
        # print("P:", P)
        # print("qNext:", qNext)
        # print("b", b)
        # print()
    
    gcd = euclAlg(N, P)

    if (gcd != 1 and gcd != N):
        factor = int(gcd)
       
    return factor

def isPerfectSquare(integer):
    root = sqrt(integer)
    return integer == int(root + 0.5) ** 2

def euclAlg(a, m):
    dividend = []
    divisor = []
    q = []
    r = []
    i = 0
    j = 0

    maxVal = max(a, m)
    minVal = min(a, m)
    dividend.append(maxVal)
    divisor.append(minVal)

    q.append(dividend[i] // divisor[i])
    r.append(dividend[i] % divisor[i])

    while r[j] != 0:
        j = j + 1
        dividend.append(divisor[i])
        divisor.append(r[i])
        q.append(dividend[j] // divisor[j])
        r.append(dividend[j] % divisor[j])
        i = i + 1

    gcd = r[j - 1]
    return gcd


# f = shanksSQUFOF(10187)
# print(f)