# Python Program for implementation of RSA Algorithm

def message_to_num(m):
    """Converts each letter in a string to its ascii value to create a number
     NOTE: ALL LETERS WILL BE CAPITALISED!"""
    upper_m = m.upper()
    num_m = ""
    for char in upper_m:
        num_m += str(ord(char))
    return int(num_m)

def power(base, expo, m):
    res = 1
    base = base % m
    while expo > 0:
        if expo & 1:
            res = (res * base) % m
        base = (base * base) % m
        expo = expo // 2
    return res



def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def modInverse(e, phi):
    gcd, x, y = egcd(e, phi)
    if gcd != 1:
        return None  # modular inverse does not exist
    else:
        return x % phi


# RSA Key Generation
def generateKeys(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e, where 1 < e < phi(n) and gcd(e, phi(n)) == 1
    e = 0
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    # Compute d such that e * d ≡ 1 (mod phi(n))
    d = modInverse(e, phi)

    return e, d, n


# Function to calculate gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


# Encrypt message using public key (e, n)
def encrypt(m, e, n):
    return power(m, e, n)


# Decrypt message using private key (d, n)
def decrypt(c, d, n):
    return power(c, d, n)


# Main execution
if __name__ == "__main__":
    print(122766192202452708561835475490908192044230647591154046992384/3)
    """# Key Generation
    p = 210524162090436900027996732083
    q = 874718067869911652116307648723
    e, d, n = generateKeys(p, q)

    print(f"Public Key (e, n): ({e}, {n})")
    print(f"Private Key (d, n): ({d}, {n})")

    # Message
    M = message_to_num("WE STRIKE AT DAWN")
    print(f"Original Message: {M}")

    # Encrypt the message
    C = encrypt(M, e, n)
    print(f"Encrypted Message: {C}")

    # Decrypt the message
    decrypted = decrypt(C, d, n)
    print(f"Decrypted Message: {decrypted}")"""