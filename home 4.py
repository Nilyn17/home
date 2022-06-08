'''

a = input('string: ')
def adr(a):
    for c in a:
        if c == ' ':
            print ('[.]', end='')
        else:
            print (c, end='')
        continue    
    
adr(a)
print ()
'''