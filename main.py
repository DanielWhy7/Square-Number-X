import random

VERSION=1.35

running=True

m_procedural={'p','proced','procedural'}
m_random={'r','ran','rand','random','rng'}
m_reverse={'e','rev','reverse'}
m_remember={'qr','remem','remember'}

a_true={'t','true'}

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
    if checkInside(mode,m_remember):
        running=False
        while prevnumber<=maximal-1:
            prevnumber+=1
            number=prevnumber

            print(str(number)+'x'+str(number)+': '+str(number**2))
    else:
        if checkInside(mode,m_random):
            number=random.randint(minimal,maximal)
        elif checkInside(mode,m_reverse):
            if prevnumber<=minimal:
                prevnumber=maximal+1
            prevnumber-=1
            number=prevnumber
        else:
            if prevnumber>=maximal:
                prevnumber=minimal-1
            prevnumber+=1
            number=prevnumber

        correct=number**2
        answer=input(str(number)+'x'+str(number)+': ')
        if answer==str(correct):print(' [+] Correct.')
        elif answer=='exit':break
        else:
            print(' [-] Wrong. Right answer is '+str(correct)+'.')
            if checkInside(error_fix,a_true):
                prevnumber=minimal-1

        print('_______________________________\n')
