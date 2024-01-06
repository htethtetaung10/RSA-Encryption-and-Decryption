from math import sqrt
import random
from math import floor
from shanksSQUFOFAlg import shanksSQUFOF

def main():
    m = []
    c = []
    plaintext = []

    #Input
    mSize = int(input("Enter message size which you want to encrypt:"))

    #Plaintext sequence
    for i in range(0, mSize):
        m.append(int(input("Enter a message:")))

    print("Original Message:")
    print(m)
    print()

    # Encryption
    c,n,e = encryptionAlg(m)
    print("Encrypted Message:")
    print(c)
    print()

    # Breaking public key (n)
    prime1 = shanksSQUFOF(n)
    prime2 = int(n / prime1)
    nAfterbreak = prime1 * prime2
    print("Breaking public key:")
    print("Two primes after breaking:", prime1, prime2)
    print("n after breaking:", nAfterbreak)
    print()

    # Decryption
    plaintext = decryptionAlg(c, nAfterbreak, e)
    print("Decrypted Message(Plaintext):")
    print(plaintext)

#****************************************************************

def encryptionAlg(m):
    #Choosing random p and q
    min = int(input("Enter minimum value for p and q:"))
    max = int(input("Enter maximum value for p and q:"))
    p = randomPrime(min, max)
    q = randomPrime(min, max)
    print("p and q:", p, q)
    print()

    #Public keys
    n = p * q
    phi = eulerPhi(n)
    e = randomPubExponent(1, phi-1, phi)
    print("Public key(n):", n)
    print("Public key(e):", e)
    print("Phi(n):", phi)
    print()

    # Encryption
    c = []
    for i in m:
        c.append((i ** e) % n)
    
    return c, n, e

#***************************************************************

def decryptionAlg(c, n, e):
    plaintext = []

    _,d = extendedEuclAlg(e, eulerPhi(n))
    print("d for decryption:", d)
    print()

    for i in c:
        plaintext.append((i ** d) % n)

    return plaintext

#***************************************************************

def eulerPhi(a):
    num = 1 #phi(1) = 1
    for i in range(2, a):
        g,_ = extendedEuclAlg(i, a)
        if g == 1:
            num += 1
    return num

def isPrime(a):
    if a == 1:
        return False

    for i in range(2, (int(sqrt(a)) + 1)):
        if a % i == 0:
            return False

    return True

def randomPrime(min, max):
    n = random.randint(min, max)
    while isPrime(n) == False:
        n = random.randint(min, max)
    return n

def randomPubExponent(min, max, phi):
    e = random.randint(min, max)
    gcd,_ = extendedEuclAlg(e, phi)
    while gcd != 1:
        e = random.randint(min, max)
        gcd,_ = extendedEuclAlg(e, phi)  
    return e

def isPerfectSquare(integer):
    root = sqrt(integer)
    return integer == int(root + 0.5) ** 2

def extendedEuclAlg(a, m):
    # finding GCD
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

    #finding inverse
    i = 1
    v = [1]
    z = [-q[len(q)-i-1]]

    while(i < len(q)):
        v.append(z[i-1])
        z.append(v[i-1]+z[i-1]*(-q[len(q)-i-2]))
        i = i+1
    
    inv = v[len(v)-1] % m

    return gcd,inv


if __name__ == '__main__':
    main()