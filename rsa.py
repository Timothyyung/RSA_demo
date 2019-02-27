import gmpy2
import numpy

#This inverse mode is found on https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
def __inversemod(a,p):
    a = a%p
    for x in range(1,p):
        if (( a*x) % p == 1):
            return x
    return 1




#Choose two prime numbers to be a public and private key, To demonstrate the rsa algroithm we will use two smaller prime numbers since python cannot handle numbers that are too large.
p = 7
q = 23
print ('p({p}) and q({q})'.format(p=p,q=q))
#Muliply the two primes to create n
n = p*q
print ('n is the product of the two numbers\nn:{}\n'.format(n))
#choose an e value between the 1 and the lcm(53,71), Idealy should be prime
lcm_ = numpy.lcm((p-1),(q-1))
e = 13
#Modular inversion https://gmpy2.readthedocs.io/en/latest/intro.html
d = gmpy2.invert(gmpy2.mpz(e),gmpy2.mpz(int(lcm_)))
dt = __inversemod(e,int(lcm_))

print ('lcm:{}\n'.format(lcm_))
print ('e:{}\n'.format(e))
print ('d:{d} \nd\':{dt}\n\n'.format(d=d, dt=dt))



#message to encrypt: we will encrypt a number

m = 14

print('Formula for encrpytion is c(m) = m^e % n\norignal number:{}'.format(m))
#encrypting
cm = m**e % n

print ('encrypted number:{} '.format(cm))

#decryption


mc = cm**d % n

print ('Formula for decripytion is m(c) = cm ^ d % n\ndecrpyted number:{} '.format(mc))
