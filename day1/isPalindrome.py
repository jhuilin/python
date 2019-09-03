num = int(input('Enter a whole number: '))
temp = num
num2 = 0
while temp > 0:
    num2 *= 10
    num2 += temp % 10
    temp //= 10
if num == num2:
    print('%d is palidrome' %num)
else:
    print('%d is not palidrome' %num)
