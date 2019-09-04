a = int(input('enter a whole number'))
b = int(input('enter another whole number'))

(a,b) = (b, a) if a > b else (a, b)
for factor in range(a,0,-1):
    if a % factor == 0 and b % factor == 0:
        print('the gcd is %d' %factor)
        break
        
print('over')