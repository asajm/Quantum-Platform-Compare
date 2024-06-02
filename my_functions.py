import math
import random
from sympy import isprime


def find_all_as(N):
    ns=[]
    for n in range(2,N):
        if math.gcd(n,N)==1:
            ns.append(n)
    return ns

def validate_a(a):
    ns = find_all_as(N)
    if a not in ns:
        raise ValueError(f"'a' must be one of {ns}")
    return True

def get_nlen_mlen(N):       
    n_len = math.ceil(math.log2(N))
    m_len = 2 * n_len
    return n_len, m_len 

# this function just to print what inside controlled U gate
def print_c_amodN(a, N):
    n_len, m_len = get_nlen_mlen(N)
    
    for p in range(m_len):
        pwr = 2**p
        _txt = f'a={a}, N={N}, j={p}, 2^j={pwr}'
        print(f"\n{_txt}\n{len(_txt)*'-'}")
    
        print(f"{format(pow(a,pwr,N), f'0{n_len}b')} | {a}^{pwr} mod {N} = {pow(a,pwr,N)}")
        print(f"{format(pow(a,pwr,N)^1, f'0{n_len}b')} | x_gates")
        

def is_power_of_prime(N):
    for base in range(2, int(math.sqrt(N)) + 1):
        power = 2
        while (result := base ** power) <= N:
            if result == N:
                return True
            power += 1
    return False

def validate_N(N):
    if isprime(N):
        raise ValueError(f"{N} is a prime.")
    if is_power_of_prime(N):
        raise ValueError(f"{N} is a power of a prime.")
    return True


def check_r_condition(a, r, N):
    if r % 2 == 0 and pow(a, r // 2, N) != N - 1:
        return True
    else:
        return False
    
    
# 100 of prime numbers
prime_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 
             107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 
             227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 
             349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 
             467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

def generate_N():
    ACCEPTED_N = False
    max_qubits = 29
    while not ACCEPTED_N:
        ps = random.sample(prime_100[5:], 2)
        N = ps[0]*ps[1]
        n_len, m_len = get_nlen_mlen(N)
        if n_len+m_len<=max_qubits:
            print(f"N = {ps[0]} * {ps[1]} = {N}")
            return N