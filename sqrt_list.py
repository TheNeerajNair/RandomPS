import math as m
C = 50
H = 30
op = []
D = input("Enter Your Values")
num = D.split(',')
print(num)
for a in num:
    z = m.sqrt((2 * C * int(a) )/H)
    
    op.append(z)

print(op)
