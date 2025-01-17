Python 3.11.3 (tags/v3.11.3:f3909b8, Apr  4 2023, 23:49:59) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#Method of dict
#method is use to helps you manipulate and fromat string easily.

#1)keys()
details={'name':'sumit','age':21,'type':'student'}
details.keys()
dict_keys(['name', 'age', 'type'])

#keys() always return list of all keys.

student={'Roll_No':01,'Name':'sumit','College_name':'GSG'}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
student={'Roll_No':1,'Name':'sumit','College_name':'GSG'}
student.keys()
dict_keys(['Roll_No', 'Name', 'College_name'])

#Values()
#values() always return list of all values in dict.
student.values()
dict_values([1, 'sumit', 'GSG'])

#items()
#items() is return list of tuples of key and value.

student.items()
dict_items([('Roll_No', 1), ('Name', 'sumit'), ('College_name', 'GSG')])

#4)clear()
#clear() function is used for removing all the elements from non-empty dict.

#if we call this function on empty dict the we get space or none as result.

print(student)
{'Roll_No': 1, 'Name': 'sumit', 'College_name': 'GSG'}

student.clear()
print(student)
{}

print(student)
{}

student={'Roll_No':1,'Name':'sumit','College_name':'GSG'}
student.clear()
print(student)
{}

#pop(key)
#syntax :-dictobj.pop(key)
#this function is use to removing key, values form non-empty dict.

#if we call this funtion on empty dict object then we get keyerror.

student={'Roll_No':1,'Name':'sumit','College_name':'GSG'}
student.pop('Name')
'sumit'
student.pop('Roll_No')
1
student.pop('College_name')
'GSG'

#3)popitem()
#dictobj.popitem()
#this is used for removing last key,values entry of non-empty dict object.

#if we call this function on empty dict object then we get keyerror.

student={'Roll_No':1,'Name':'sumit','College_name':'GSG'}
student.popitem()
('College_name', 'GSG')
student.popitem()
('Name', 'sumit')
student.popitem()
('Roll_No', 1)

#4)get()
#varname=dictobj.get(key)
#This is use for obtaning value of value by passing value of key.

#if the value of key does not exist then we get keyerror.

student={'Roll_No':1,'Name':'sumit','College_name':'GSG'}
print(studnet)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    print(studnet)
NameError: name 'studnet' is not defined. Did you mean: 'student'?
>>> print(student)
{'Roll_No': 1, 'Name': 'sumit', 'College_name': 'GSG'}
>>> 
>>> student.get('name')
>>> print(student)
{'Roll_No': 1, 'Name': 'sumit', 'College_name': 'GSG'}
>>> 
>>> stu=student.get('name')
>>> print(stu)
None
>>> student.get('Name')
'sumit'
>>> student.get('College_name')
'GSG'
>>> student.get('Roll_No')
1
>>> 
>>> 
>>> print(student)
{'Roll_No': 1, 'Name': 'sumit', 'College_name': 'GSG'}
>>> 
>>> student[percentage]=89
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    student[percentage]=89
NameError: name 'percentage' is not defined
>>> 
>>> student['College_name']=UKD
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    student['College_name']=UKD
NameError: name 'UKD' is not defined
>>> 
>>> STU={}
>>> print(type(STU))
<class 'dict'>
>>> STU.keys()
dict_keys([])
