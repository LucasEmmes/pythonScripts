import math

def is_prime(x):
    if x % 2 == 0:
        return False

    for i in range(3, math.ceil(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False

    return True

def get_distinct_factors(n):
    factors = []
    
    while not is_prime(n):
        for i in range(2, math.ceil(math.sqrt(n))+1):
            if n % i == 0:
                n = n//i
                factors.append(i)
                break
    
    factors.append(n)
    return set(factors)

class group:

    def __init__(self, n):
        self.n = n
        self.is_prime = is_prime(n)
        self.group = self.get_group()
        self.order = len(self.group)

    def get_group(self):
        if self.is_prime:
            return set([i for i in range(1, self.n)])

        else:
            group = []
            
            for i in range(1, self.n):
                if math.gcd(i, self.n) == 1:
                    group.append(i)

            return set(group)
    
    # Need to add way to find generators for composite integers
    def get_generators(self):
        if self.is_prime:
            generators = []

            factors = get_distinct_factors(self.n-1)
            print(factors)

            for i in range(1, self.n):
                gen = True
                for f in factors:
                    if i**((self.n - 1) // f) % self.n == 1:
                        print(f"Found a fucker: {i}**{self.n-1}/{f} % {self.n} = {i**((self.n - 1) // f) % self.n}")
                        gen = False
                        break
                if gen:
                    generators.append(i)
            
            return set(generators)
        
        else:
            return 0

# TESTIUNG

t = group(12)
print(t.get_generators())
