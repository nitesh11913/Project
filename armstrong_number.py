armstrong_number=int(input('Enter a number: '))
n=len(str(armstrong_number))
print('n is: ',n)
sum = 0
temp=armstrong_number
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10
if armstrong_number == sum:
    print('The number is an armstrong number.')
else:
    print('The number is not an armstrong number.')