
import sympy
x = sympy.Symbol('x')

with open('file1.txt','r') as f:
   a = eval(f.readline())

with open('file2.txt','r') as f:
   b = eval(f.readline())

sum = sympy.simplify(a+b)
with open('result.txt','w') as f:
   f.write(str(sum))
