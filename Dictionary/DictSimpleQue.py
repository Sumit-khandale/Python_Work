Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#how to delete data form the dict
d={1:2,2:4,3:6}
d.pop(2)
4

print(d)
{1: 2, 3: 6}

details={1:{'name':'raj','city':'pune'},2:{'name':'rajesh','city':'nashik'}}
details[2].pop(city)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    details[2].pop(city)
NameError: name 'city' is not defined
details[2].pop('city')
'nashik'

print(details)
{1: {'name': 'raj', 'city': 'pune'}, 2: {'name': 'rajesh'}}

details={1:{'name':'raj','city':'pune'},2:{'name':'rajesh','city':'nashik'}}
details[1][percentage]=89
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    details[1][percentage]=89
NameError: name 'percentage' is not defined
details[1].add[percentage]=89
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    details[1].add[percentage]=89
AttributeError: 'dict' object has no attribute 'add'
>>> 
>>> #how to access element from the dict
>>> details={1:{'name':'raj','city':'pune'},2:{'name':'rajesh','city':'nashik'}}
>>> for i in details.values
SyntaxError: incomplete input
>>> for i in details.values():
...     print(i)
... 
...     
{'name': 'raj', 'city': 'pune'}
{'name': 'rajesh', 'city': 'nashik'}
>>> 
>>> for i in details.items():
...     print(i)
... 
...     
(1, {'name': 'raj', 'city': 'pune'})
(2, {'name': 'rajesh', 'city': 'nashik'})
>>> 
>>> for i,j in details.items():
...     print(i)
...     print(j)
... 
...     
1
{'name': 'raj', 'city': 'pune'}
2
{'name': 'rajesh', 'city': 'nashik'}
>>> 
>>> for i,j in details.items():
...     print(i)
... 
...     
1
2
>>> 
