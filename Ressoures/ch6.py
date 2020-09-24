def div(a,b):
    if(a < 0 or b <=0):
        raise ValueError('a and b have to be in N, b > 0')
    #a = b x d + r,  0 <= r < b  <= a
    d = max(a-1,b)
    while(d * b > a):
        d -= 1
    return d

def divRecursive(a,b,d=None):
    if(a < 0 or b <=0):
        raise ValueError('a and b have to be in N, b > 0')
    if(d is None): d = max(a-1,b)
    if(d*b <= a): return d # Cas de base
    return divRecursive(a,b,d-1) # Cas général

print('DIVISION')
print(div(0,4) , 0 // 4 , divRecursive(0,4))
print(div(12,4), 12 // 4, divRecursive(12,4))
print(div(13,4), 13 // 4, divRecursive(13,4))

def mod(a,b):
    d = div(a,b)
    r = a - b * d
    return r

print('MODULO')
print(mod(0,4), 0 % 4)
print(mod(12,4), 12 % 4)
print(mod(13,4), 13 % 4)

def pgcd(a,b):
    if(a < b): return pgcd(b,a)
    # a toujours >= b
    r = mod(a,b)
    if(r == 0): return b # a = b *d + 0
    return pgcd(b,r)

print('PGCD')
print(pgcd(24,36),pgcd(36,24),12)
print(pgcd(2,3),pgcd(3,2),1)

def isPrime(p):
    if(p < 2): return False
    for i in range(1,p):
        if(pgcd(p,i) > 1):
            return False
    return True

print('NOMBRES PREMIERS')
primes = [2,3,5,7,11,13,17,19,23]
for p in primes:
    print(p,isPrime(p),end=' ')
print('')
for p in filter(lambda x: x not in primes,range(max(primes))):
        print(p,isPrime(p),end=' ')
print('')

def toBase(value,digits=range(10)):
    digits = list(digits)
    base   = len(digits)
    number = ''
    while(value > 0):
        r      = mod(value,base)
        value  = div(value - r,base)
        number = str(digits[r]) + number
    return '0' if(len(number)<1)else number

print('CHANGEMENT DE BASE')
binary = range(2)
octal  = range(8)
hexa   = list(range(10)) + list('ABCDEF')
for number in [0,3,10,42]:
    print(number,toBase(number,binary),toBase(number,octal),toBase(number,hexa))