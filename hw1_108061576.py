# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
from random import randint

# Miller-Rabin Test
def isprime(n):
    # n-1 = m*2^k
    k = 0
    m = n-1
    while(m % 2 == 0):
        m //= 2
        k += 1
    for _ in range(100):
        a = randint(2, n-2)
        y = pow(a, m, n)
        if y == 1 or y == n-1:
            continue
        for _ in range(k-1):
            y = pow(y, 2, n)
            if y == 1: 
                return 0
            if y == n-1:
                break
        if y != n-1: 
            return 0
    return 1
    

# generate 128-bit prime number
def big_prime_number(num_of_bits):
    # keep creating a random (128-bit) number until there is a prime number
    while (1):
        num = random.getrandbits(num_of_bits)
        
        if isprime(num):
            return num
        else:
            continue

def SQRT_3_mod4(p, a):
    return pow(a, (p+1)//4, p)

def SQRT_5_mod8(p, a):
    d = pow(a, (p-1)//4, p)
    if d == 1:
        return pow(a, (p+3)//8, p)
    elif d == p - 1:
        return 2*a*pow(4*a, (p-5)//8, p) % p
    
def ext_euclid(a, b):
    old_s = 1
    s = 0
    old_t = 0
    t = 1
    old_r = a
    r = b
    if b == 0:
        return 1, 0, a
    else:
        while(r!=0):
            q=old_r//r
            old_r,r=r,old_r-q*r
            old_s,s=s,old_s-q*s
            old_t,t=t,old_t-q*t
    return old_s, old_t

def encryption(m, n):
    return pow(m, 2, n)

def decryption(a, p, q):
    n = p * q
    r = 0
    s = 0
    
    if pow(p, 1, 4) == 3:
        r = SQRT_3_mod4(p, a)
    elif pow(p, 1, 8) == 5:
        r = SQRT_5_mod8(p, a)
        
        
    if pow(q, 1, 4) == 3:
        s = SQRT_3_mod4(q, a)
    elif pow(q, 1, 8) == 5:
        s = SQRT_5_mod8(q, a)
    
    c, d = ext_euclid(p, q)
    
    x = pow(r * d * q + s * c * p, 1, n)
    y = pow(r * d * q - s * c * p, 1, n)
    
    return x, n-x, y, n-y

def choose(candidate):

    for i in candidate:
        candidate_bin = bin(i)
        append = candidate_bin[-16:]
        #append2 = candidate_bin[-33:-17]
        candidate_bin = candidate_bin[:-16]   
        if append == candidate_bin[-16:]:
            return i
    return

def print_space(text):
    for i in range(0, len(text)):
        if (i+1)%8==0:
            print(str(text[i])+' ', end='')
        else:
            print(text[i], end='')
    print('\n')

def space(text):
    return (text.replace(' ', ''))      
   
if __name__ == "__main__":
    
    print('<Miller-Rabin>')
    print_space(hex(big_prime_number(256))[2:])
    
    #input p and q
    print('<Rabin Encryption>')
    p = int(space(input('p = ')), 16)
    q = int(space(input('q = ')), 16) 
    print()
    n = p * q
    print('n = pq = ', end='')
    n_hex = hex(n)[2:]
    print_space(n_hex)
    
    #generate p and q
    #p = big_prime_number(128) 
    #p_hex = hex(p)[2:]
    #print(p_hex)
    #q = big_prime_number(128)
    #q_hex = hex(q)[2:]
    
    #padding the last 16-bit of plaintext
    plaintext = int(space(input('Plaintext = ')), 16)
    plaintext_bin = bin(plaintext)[2:]
    plaintext_pad = plaintext_bin + plaintext_bin[-16:]
    plaintext_pad_int = int(plaintext_pad, 2)
   
    # Encryption
    cipher = encryption(plaintext_pad_int, n)
    cipher_hex = hex(cipher).split('x')[-1]
    #cipher_hex = hex(int(str(cipher), 10))[2:]
    
    #print result

    print('Ciphertext = ', end='')
    print_space(hex(cipher)[2:])
    
    print('<Rabin Decryption>')
    cipher_decy = int(space(input('Ciphertext = ')), 16)
    #cipher_decy_int = int(cipher_decy, 16)
    print()
    print('Private Key:')
    p_decy = int(space(input('p = ')), 16)
    q_decy = int(space(input('q = ')), 16)
    print()
    
    # choose from 4 candidates
    r1, r2, r3, r4 = decryption(cipher_decy, p_decy, q_decy)
    candidate = [r1, r2, r3, r4]
    plaintext_final = choose(candidate)
    plaintext_final = bin(plaintext_final)
    plaintext_final = plaintext_final[:-16]
    plaintext_final = hex(int(plaintext_final, 2))
    print('Plaintext = ', end='')
    print_space(plaintext_final[2:].zfill(226//4))


    