from random import randint as rint
from typing import List

VERSION="1.4.2"

run=True

#TODO: Add language support
m_proc:List[str]=['p','pro','proced','procedural']
m_rand:List[str]=['r','ran','rand','random','rng']
m_reve:List[str]=['e','rev','reverse']
m_reme:List[str]=['qr','rem','remem','remember']

m_true:List[str]=['t','true','1','y','yes','yeah','ye','sure']

m_exit:List[str]=['q','^c','exit','break','ctrl+c','escape','ctrlc']
m_menu:List[str]=['menu','configuration','home','m']
m_errr:List[str]=['er','error','mistake']

dline:str='_______________________________'

mistakes:int=0

def chek(s:str,array:List[str])->bool:#CHEcK
  """
  Return True if `s` is a member of `array`, otherwise False
  Example: You can say in prompt yeah, yes, ye, true instead of yes
  """
  return s in array

def chex(text:str)->str:#CHeck EXit
  """
  Return `text`, or exit the program if it is an exit command
  """
  if chek(text,m_exit):exit()
  return text

def is_n(text:str)->int:#IS Number
  """
  Parse `text` as an integer, falling back to 11 when it is not numeric
  """
  return int(text) if text.isnumeric() else 11

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
          print(f' [*] Mistakes: {mistakes}')
          prevnumber=number-1#IDK
        else:
          mistakes+=1
          print(' [-] Wrong. Right answer is '+str(correct))
          if chek(error_fix,m_true):
            prevnumber=minimal-1

        print(dline+'\n')
