def message_to_num(m):
    """Converts each letter in a string to its ascii value to create a number
     NOTE: ALL LETERS WILL BE CAPITALISED!"""
    upper_m = m.upper()
    num_m = ""
    for char in upper_m:
        num_m += str(ord(char))
    return int(num_m)

def create_padlock(p1, p2, e=3):
    """Returns 2 values n (our modulo), e (our exponent) for encrypting message"""
    n = p1 * p2
    return n, e

def create_key(p1, p2, e):
    t = (p1-1)*(p2-1)
    k=0
    d = 0.1
    while d != int(d):
       k += 1
       d = ((k*t)+1)/e
    return int(d)

def decrypt_message_to_num(c, d, n):
    return pow(c,d,n)

def encrypt_message(num_m,e,n):
    return pow(num_m, e, n)

def validate_e(e, t):
    # Assumes prime input
    if t/e == int(t/e):
        return False
    if t <= e:
        return False
    return True

def main():
    print("Alice Side: ")
    p1 = int(input("Enter prime number 1: "))
    p2 = int(input("Enter prime number 2: "))

    n, e = create_padlock(p1, p2)
    d = create_key(p1, p2, e)

    input("Press enter to send off n and e to Bob. ")
    print("n and e sent off but Alice now also has them!")

    print("Bob Side")
    m = input("Enter Message: ")
    num_m = message_to_num(m)
    print(num_m)
    c = encrypt_message(num_m, e, n)

    input("Press enter to send off c to Alice. ")
    print("c sent off but Alice now also has it!")

    print("Alice silde")
    decrypted_m = decrypt_message_to_num(c, d, n)
    print(decrypted_m)

def test():
    p11 = 93333257
    p21 = 84784369
    e = 65537
    p1 = 731742727
    p2 = 757461871
    n, e = create_padlock(p1, p2, e)
    if not validate_e(e, ((p1-1)*(p2-1))):
        return -1
    print(f"modulo {n}, exponent {e}")
    d = create_key(p1, p2, e)
    print(f"private key {d}")
    num_m = message_to_num("zzzzzzz")
    print(num_m)
    c = encrypt_message(num_m, e, n)
    print(f"cypher text {c}")
    decrypted_m = decrypt_message_to_num(c, d, n)
    print(decrypted_m)

print(test())