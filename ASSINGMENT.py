print('Yusuf and sons')
principal = float(input('Enter Principal: '))
time = float(input('Enter time: '))
rate = float(input('Enter rate: '))
simple_interest = (principal*time*rate)/100
compound_interest = principal * ( (1+rate/100)**time - 1)
print('Simple interest is: %f' % (simple_interest))
print('Compound interest is: %f' %(compound_interest))

print(f"""Therefore the simple interest and compound interest are {simple_interest} and
{compound_interest} respectively.""")