import random

VERSION=1.35 #1.4

running=True

m_procedural={'p','proced','procedural'}
m_random={'r','ran','rand','random','rng'}
m_reverse={'e','rev','reverse'}
m_remember={'qr','remem','remember'}

a_true={'t','true','1','y','yes','yeah'}

a_exit={'exit','break','ctrl+c','escape','ctrlc'}
#a_menu={'menu','configuration','home'}

mistake_count=0

def checkInside(s,array):
    for x in array:
        if x==s:return True
    return False

def exitCheck(text):
    if checkInside(text,a_exit):exit()
    return text

def isNumber(text):
    if text.isnumeric():return int(text)
    return 0

print('\nSquare Number X\n_______________\n')

minimal=isNumber(exitCheck(input('Enter minimum: ')))
maximal=isNumber(exitCheck(input('Enter maximum: ')))

print()

mode=exitCheck(input('Procedural | Random | Reverse | Remember\nMode: ')).lower()
if checkInside(mode,m_random):skip_number_with_zero=exitCheck(input('\nSkip numbers that ends at 0\nEnable: '))
elif not checkInside(mode,m_remember):error_fix=exitCheck(input('\nError corrector\nEnable: ')).lower()
else:error_fix=False

print('_______________________________\n')

prevnumber=minimal-1

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
        answer=exitCheck(input(str(number)+'x'+str(number)+': '))
        if answer==str(correct):print(' [+] Correct.')
        else:
            print(' [-] Wrong. Right answer is '+str(correct)+'.')
            if checkInside(error_fix,a_true):
                prevnumber=minimal-1

        print('_______________________________\n')
