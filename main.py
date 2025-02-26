import random
running=True

m_procedural={'p','proced','procedural'}
m_random={'r','ran','rand','random','rng'}
m_reverse={'e','rev','reverse'}

print('\nSquare Number X\n_______________\n')

minimal=int(input('Enter minimum: '))
maximal=int(input('Enter maximum: '))
print()
mode=input('Mode(random,procedural): ').lower()
error_fix=input('Error Restart: ').lower()

print('_______________________________\n')

prevnumber=minimal-1

def checkInside(s,array):
    for x in array:
        if x==s:
            return True
    return False

while running:
    if checkInside(mode,m_random):
        number=random.randint(minimal,maximal)           else:
        if prevnumber>=maximal:
            prevnumber=minimal-1
        prevnumber+=1
        number=prevnumber

    correct=number**2
    answer=input(str(number)+'x'+str(number)+': ')
    if answer==str(correct): print(' [+] Correct.')
    elif answer=='exit': break
    else:
        print(' [-] Wrong. Right answer is '+str(corr
ect)+'.')
        if error_fix=='true':
            prevnumber=minimal-1

    print('_______________________________\n')import random
running=True

m_procedural={'p','proced','procedural'}
m_random={'r','ran','rand','random','rng'}
m_reverse={'e','rev','reverse'}

print('\nSquare Number X\n_______________\n')

minimal=int(input('Enter minimum: '))
maximal=int(input('Enter maximum: '))
print()
mode=input('Mode(random,procedural): ').lower()
error_fix=input('Error Restart: ').lower()

print('_______________________________\n')

prevnumber=minimal-1

def checkInside(s,array):
    for x in array:
        if x==s:
            return True
    return False

while running:
    if checkInside(mode,m_random):
        number=random.randint(minimal,maximal)           else:
        if prevnumber>=maximal:
            prevnumber=minimal-1
        prevnumber+=1
        number=prevnumber

    correct=number**2
    answer=input(str(number)+'x'+str(number)+': ')
    if answer==str(correct): print(' [+] Correct.')
    elif answer=='exit': break
    else:
        print(' [-] Wrong. Right answer is '+str(corr
ect)+'.')
        if error_fix=='true':
            prevnumber=minimal-1

    print('_______________________________\n')
