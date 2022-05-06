
from Crypto.Util.number import long_to_bytes,inverse


""" 
DEPENDENCIES: 
pip3 install pycryptodome

I got some insight from here: 
https://www.educative.io/edpresso/what-is-the-rsa-algorithm 
https://en.wikipedia.org/wiki/RSA_(cryptosystem)
"""
# we know that the RSA factors are started with these tokens, so we use them to get our integers
C_TOK = b"c: " 
N_TOK = b"n: "
E_TOK = b"e: "
C = None
N = None
E = None


with open('values', mode='rb') as file:
    data = file.read().split(b'\n') # File.read() will return a bytes array
    
    for line in data:

        if C_TOK in line: # Get c by stripping C_TOKEN Defined above, same logic for other tokens
            C = int(line.strip(C_TOK))
        elif N_TOK in line:
            N = int(line.strip(N_TOK))
        elif E_TOK in line:
            E = int(line.strip(E_TOK))
        else: # This else will skip first line.
            continue

print("E:" + str(E))
print("C:" + str(C))
print("N:" + str(N) )


# n and p were extracted from http://factordb.com/



p = int(b'2434792384523484381583634042478415057961')
q = int(b'650809615742055581459820253356987396346063')

# φ(n) = (p − 1)(q − 1)

phi = (p-1)*(q-1)
print("Phi:" + str(phi))

# n = p*q (p and q being prime numbers)
# e.d=1 mod (phi) => d = 1/e mod (phi) 
# P=C^d mod n
d = inverse(E,phi)
print("D: " + str(d))

message = pow(C,d,N)

print("Decrypted: ")
print(long_to_bytes(message))










        