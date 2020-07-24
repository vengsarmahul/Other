#Calculate Prime using Sieve of Eratosthenes -

def sieve(n):
    is_prime = [0] * 2 + [1] * (n - 1) 
    
    for i in range(int(n**0.5 + 1.5)): # stop at ``sqrt(n)``
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = 0
    return [i for i, prime in enumerate(is_prime) if prime]

def main():
    try:
        n = int(input('Enter a number: '))
        print (sieve(n))
    except ValueError:
        print ('Enter only an integer value, n > 1.')
        main()
        
if __name__ == '__main__':
    main()
