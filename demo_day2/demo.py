"""
This is a comment describing scripts's purpose
"""

name = 'abcdef'
print('type ',type(name), 'value ',name, sep="*")

number = 1000
print('type ',type(name), 'value ',number, sep="*")
print('type ',type(name), 'value ',10.5, sep="*")

# comparadores logicos
# == != > < <= >= not
resutado =not 1 == 0
print('type ',type(name), 'value ',resutado, sep="*")
resutado =1 == 0
print('type ',type(name), 'value ',resutado, sep="*")

#NOne 
test = None
if test:
    print(test)
else:
    print("unidefined")


# all strings are sequences (list)
# print all caracters in string
str = "abcdefghijklm"
print(str)

#for loops
for character in str:
    print(character)

#not en vez de !

names = ['x', 'asas', 'nnnnn']
for name in names:
    print(name)
print("&&")
print(*names, sep='\n')
# aprender a leer la documentacion
