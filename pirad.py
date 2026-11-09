from random import randint as rint
# Current version
VERSION='1.1.2'

run=True
lrun=True

m_pro=['p','proced','procedural']
m_ran=['r','ran','rand','random','rng']
m_rev=['e','rev','reverse']
m_rem=['qr','remem','remember']

m_sin=['sin','synapse','s']
m_cos=['cos','c']
m_tan=['tan','tg','t']
m_ctg=['ctan','ctg','ct']

m_men=['m','menu','home','conf','config','configuration']
m_yes=['t','true','1','y','yes','yeah']
m_ext=['exit','break','ctrl+c','escape','ctrlc','c','q','quit']

dline='_______________________________'

k=0 #TODO

# Data
deg=[0,30,45,60,90,120,135,150,180,210,225,240,270,300,315,330,360]
a=['0','π/6','π/4','π/3','π/2','2π/3','3π/4','5π/6','π','7π/6','5π/4','4π/3','3π/2','5π/3','7π/4','11π/6','2π']
sin=['0','1/2','√2/2','√3/2','1','√3/2','√2/2','1/2','0','-1/2','-√2/2','-√3/2','-1','-√3/2','-√2/2','-1/2','0']
cos=['1','√3/2','√2/2','1/2','0','-1/2','-√2/2','-√3/2','-1','-√3/2','-√2/2','-1/2','0','1/2','√2/2','√3/2','1']
tan=['0','√3/3','1','√3','','-√3','-1','-√3/3','0','√3/3','1','√3','','-√3','-1','-√3/3','0']
ctg=['','√3','1','√3/3','0','-√3/3','-1','-√3','','√3','1','√3/3','0','-√3/3','-1','-√3','']

def chek(s, array):
  return s in array

def chex(text):
  if chek(text,m_ext):exit()
  if chek(text,m_men):global lrun;lrun=False
  return text

print(f'\nπRad-Pro | Version: {VERSION}\n{dline}')

while run:
  mode=chex(input('\nProcedural | Random | Reverse | Remember\nMode: ')).lower()

  func=chex(input('\nSIN | COS | TAN | CTG | A\nFunc: ')).lower()
  sfunc='sin'
  if chek(func,m_cos):
    func=cos
    sfunc='cos'
  elif chek(func,m_tan):
    func=tan
    sfunc='tan'
  elif chek(func,m_ctg):
    func=ctg
    sfunc='ctg'
  elif chek(func,['a']):
    func=a
    sfunc='a'
  else:
    func=sin
  print(dline+'\n')

  lrun=True

  if chek(mode,m_rem):
    for i in range(17):
      print(sfunc+'('+str(deg[i])+'°): '+func[i])
  elif chek(mode,m_ran):
    while lrun:
      if not lrun:break
      i=rint(0,16)
      ans=chex(input(sfunc+'('+str(deg[i])+'°): '))

      if ans.replace('s','√').replace('p','π')==func[i]:
        print('Right.')
      else:
        k+=1
        print('Wrong.Correct is '+func[i]+'.')
      print(dline)
  elif chek(mode,m_rev):
    while lrun:
      for i in range(16,-1,-1):
        if not lrun:break
        ans=chex(input('sin('+str(deg[i])+'°): '))
        if ans.replace('s','√').replace('p','π')==func[i]:
          print('Right.')
        else:
          k+=1
          print('Wrong.Correct is '+func[i]+'.')
        print(dline)
  else:
    while lrun:
      for i in range(17):
        if not lrun:break
        ans=chex(input('sin('+str(deg[i])+'°): '))
        if ans.replace('s','√').replace('p','√')==func[i]:
          print('Right.')
        else:
          k+=1
          print('Wrong.Correct is '+func[i]+'.')
        print(dline)
