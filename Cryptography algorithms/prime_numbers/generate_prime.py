def lucas_lehmer_seq(n, *args):
    if n == 0:
        return 4

    if len(args) == 0:
        return lucas_lehmer_seq(n-1)**2 - 2
    
    return (lucas_lehmer_seq(n-1, *args)**2 - 2) % args[0]

p = 2**13 - 1
l = lucas_lehmer_seq(12, p)
print(f"Result: {l}")
    