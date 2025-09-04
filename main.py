from random import randint as rint

VERSION="1.4.0"

run=True

#TODO: Add language support
m_proc=['p','proced','procedural']
m_rand=['r','ran','rand','random','rng']
m_reve=['e','rev','reverse']
m_reme=['qr','remem','remember']

m_true=['t','true','1','y','yes','yeah']

m_exit=['q','^c','exit','break','ctrl+c','escape','ctrlc']
m_menu=['menu','configuration','home','m']
m_errr=['er','error','mistake']

dline='_______________________________'

k=0

def chek(s, array):
    return s in array

def chex(text):
    if chek(text,m_exit):exit()
    return text

def is_n(text):
    if text.isnumeric():return int(text)
    return 11

print(f'\nSquare Number X | Version: {VERSION}\n{dline}\n')

while True:
    minimal=is_n(chex(input('Enter minimum: ')))
    maximal=is_n(chex(input('Enter maximum: ')))

    mode=chex(input('\nProcedural | Random | Reverse | Remember\nMode: ')).lower()
    if chek(mode,m_rand):skip_number_with_zero=chex(input('\nSkip numbers that ends at 0\nEnable: '));error_fix=False
    elif not chek(mode,m_reme):error_fix=chex(input('\nError corrector\nEnable: ')).lower()
    else:error_fix=False

    print(dline+'\n')

    prevnumber=minimal-1

    if chek(mode,m_reme):
        while prevnumber<=maximal-1:
            prevnumber+=1
            number=prevnumber

            print(str(number)+'x'+str(number)+': '+str(number**2))
    else:
        while run:
                if chek(mode,m_rand):
                    number=rint(minimal,maximal)
                elif chek(mode,m_reve):
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
                answer=chex(input(str(number)+'x'+str(number)+': '))
                if answer==str(correct):print(' [+] Correct.')
                elif chek(answer,m_menu):
                    print(' [*] Mode changed\n')
                    break
                elif chek(answer,m_errr):
                    print(f' [*] Mistakes: {k}')
                    prevnumber=number-1#IDK
                else:
                    k+=1
                    print(' [-] Wrong. Right answer is '+str(correct))
                    if chek(error_fix,m_true):
                        prevnumber=minimal-1

                print(dline+'\n')
