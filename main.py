import math
x=int(input())
root = math.sqrt(x)
if x == root * root:
	print("perfect square")
else:
	print("not a perfect square")