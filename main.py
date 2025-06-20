def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def message_to_num(m):
    """Converts each letter in a string to its ascii value to create a number
     NOTE: ALL LETERS WILL BE CAPITALISED!"""
    upper_m = m.upper()
    num_m = ""
    for char in upper_m:
        num_m += str(ord(char))
    return int(num_m)

def num_to_message(m):
    num_text = str(m)
    text = ""
    for i in range(0, len(num_text), 2):
        text += chr(int(num_text[i]+num_text[i+1]))
    return text

def create_padlock(p1, p2):
    """Returns 2 values n (our modulo), e (our exponent) for encrypting message"""
    n = p1 * p2
    t = (p1-1)*(p2-1)
    e = 0
    for e in range(2, t):
        if gcd(e, t) == 1:
            break
    return n, e, t

def create_key(t, e):
    k = 0  # Defining k
    d = 1
    # Loop to ensure that private key is an integer
    while d%e != 0:
        k += 1
        d = (1+k*t)
    return d//e

def decrypt_message_to_num(c, d, n):
    return pow(c,d,n)

def encrypt_message(num_m,e,n):
    return pow(num_m, e, n)

def main():
    print("Bob Side: ")
    m = input("Enter Message: ")
    input("Press enter for Alice to generate the keys. ")

    print("Alice Side: ")
    p1 = 427339429644236995442992359307
    p2 = 469334883452600878339466720693

    n, e, t = create_padlock(p1, p2)
    print("Generated n and e")
    d = create_key(t, e)
    print("Generated d")

    input("Press enter to send off n and e to Bob but not d.")
    print("n and e sent off but Eve now also has them!")

    print("Bob Side")
    print("Converting our sentence to numbers.")
    num_m = message_to_num(m)
    print(num_m)
    c = encrypt_message(num_m, e, n)
    print("Encrypted the message using e and n")

    input("Press enter to send off c to Alice. ")
    print("c sent off but Eve now also has it!")

    print("Alice silde")
    decrypted_m = decrypt_message_to_num(c, d, n)
    print(decrypted_m)
    print(num_to_message(decrypted_m))

def test():
    p1 = 427339429644236995442992359307
    p2 = 469334883452600878339466720693
    n, e, t = create_padlock(p1, p2)
    print(f"modulo {n}, exponent {e}")
    d = create_key(t, e)
    print(f"private key {d}")
    num_m = message_to_num("LETS FUCKING JOEEEEEEE!!!")
    print(num_m)
    c = encrypt_message(num_m, e, n)
    print(f"cypher text {c}")
    decrypted_m = decrypt_message_to_num(c, d, n)
    print(decrypted_m)
    print(num_to_message(decrypted_m))

main()