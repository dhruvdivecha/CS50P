expression = input("Expression: ")

x, y, z = expression.split(" ")

x0 = float(x)
z0 = float(z)

if y == "+":
   ans = x0 + z0
   print(round(ans,1))
elif y == "-":
   ans = x0 - z0
   print(round(ans,1))
elif y == "*":
   ans = x0 * z0
   print(round(ans,1))
elif y == "/":
   ans = x0 / z0
   print(round(ans,1))
