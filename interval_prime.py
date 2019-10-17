lower=int(input('Enter the lower range of prime numbers: '))
higher=int(input('Enter the higher range of prime numbers: '))
for num in range(lower,higher + 1):
    if num > 1:
        for i in range (2,num):
            if num % i == 0:
                break
        else:
                print(num)