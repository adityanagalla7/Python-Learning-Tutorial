a=33
#integer(int)
b="Aditya"
#string(str)
c=42.5
#float
d=a+33j
#complex
e=((1,2,3,4,5))
#tuple
f=[1,2,3,4,5]
#list
g={'name':'Adithya','age':20}
#dictionary(dict)
h={1,2,3,4,5}
#set
i=True
#bool 

print(a)
print(type(a))

print(b)
print(type(b))

print(c)
print(type(c))

print(d)
print(type(d))

print(e)
print(type(e))

print(f)
print(type(f))

print(g)
print(type(g))

print(h)
print(type(h))

print(i)
print(type(i))

#implicit type conversion
implicit=a+c
print(implicit)
print(type(implicit))

#explicit type conversion
exp=150
exp=float(exp)
print(exp)
print(type(exp))

x=int(33.33)
print(x)
print(type(x))

y=bool(1)
print(y)
print(type(y))
