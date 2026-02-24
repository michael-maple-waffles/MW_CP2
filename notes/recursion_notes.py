#MW_CP2 recursion notes

number = 10

sequence = [1,1]

for i in range(1, number):
    sequence.append(sequence[i] + sequence[i-1])

print(sequence)

recursive_sequence = [1,1]
def fibonacci1(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        recursive_sequence.append(recursive_sequence[fibonacci1(n-1)] + recursive_sequence[fibonacci1(n-2)])

print(fibonacci1)

def fibonacci2(n):
    if n == 1:
        return 1
    elif n ==2:
        return 1
    return fibonacci2(n-1) + fibonacci2(n-2)
    
print(fibonacci2)