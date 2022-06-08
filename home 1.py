

a = input('IP: ')
def adr(a):
    for c in a:
        if c == '.':
            print ('[.]', end='')
        elif c == ':':
            print ('[:]', end='')
        else:
                print (c, end='')
        continue    
    
adr(a)
print ()



