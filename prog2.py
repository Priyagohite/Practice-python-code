Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=15
type(a)
<class 'int'>
int(a)
15
b=22.5
type(b)
<class 'float'>
int(b)
22
r='pihu'
type(r)
<class 'str'>
string(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    string(a)
NameError: name 'string' is not defined
int(i)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    int(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
int(b)
22
float(a)
15.0
str(a)
'15'
type(i)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    type(i)
NameError: name 'i' is not defined. Did you mean: 'id'?
type(a)
<class 'int'>
a=float(a)
print(a)
15.0
type(a)
<class 'float'>
r=int(r)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    r=int(r)
ValueError: invalid literal for int() with base 10: 'pihu'
a=3+3j
type(a)
<class 'complex'>
b=2j+3
b=j2+3
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    b=j2+3
NameError: name 'j2' is not defined
a=15
type(a)
<class 'int'>
int(a)

