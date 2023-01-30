import translators as ts
import translators.server as tss
import ast

langs = ['uk', 'fr', 'es', 'pt', 'de', 'ru', 'ja', 'ko', 'el', 'tr', 'mn', 'ht']
    
def setPrimary(lang):
  with open('primary/en.dict', 'r') as file:
    data = file.readlines()
    file.close()
  dict = res = ast.literal_eval(data[0])
  dict2 = {}
  print(f'Processing | en -> {lang}\n---')
  for x in range(0, 9):
    print(f'\033[91mProcess Number: {x}')
    _tempname = list(dict.keys())[x]
    print(f'\033[91mProcess Name: {_tempname}')
    _temp = tss.google(dict[f'{_tempname}'], from_language='en', to_language=lang)
    print(f'\033[93mProcess Pre: {dict[_tempname]}')
    print(f'\033[92mProcess Result: {_temp}\n---')
    dict2[f'{_tempname}'] = _temp
  print(f'\033[94mProcess Finished "primary/{lang}.dict"')
  print('\n\n\n\n')
  with open(f'primary/{lang}.dict', 'w') as file:
    file.write(str(dict2))
    file.close()

def setSecondary(lang):
  with open('secondary/en.dict', 'r') as file:
    data = file.readlines()
    file.close()
  dict = res = ast.literal_eval(data[0])
  dict2 = {}
  print(f'Processing | en -> {lang}\n---')
  for x in range(0, 4):
    print(f'\033[91mProcess Number: {x}')
    _tempname = list(dict.keys())[x]
    print(f'\033[91mProcess Name: {_tempname}')
    _temp = tss.google(dict[f'{_tempname}'], from_language='en', to_language=lang)
    print(f'\033[93mProcess Pre: {dict[_tempname]}')
    print(f'\033[92mProcess Result: {_temp}\n---')
    dict2[f'{_tempname}'] = _temp
  print(f'\033[94mProcess Finished "secondary/{lang}.dict"')
  print('\n\n\n\n')
  with open(f'secondary/{lang}.dict', 'w') as file:
    file.write(str(dict2))
    file.close()

def reloadPrimary():
  for x in langs:
    setPrimary(x)

def reloadSecondary():
  for x in langs:
    setSecondary(x)

def fixFiles():
  for x in langs:
    data = ''
    with open(f'primary/{x}.dict', 'r') as file:
      data = file.read()
      file.close()
    with open(f'primary/{x}.dict', 'w') as file:
      file.write(data.replace("'", '"'))
    data2 = ''
    with open(f'secondary/{x}.dict', 'r') as file:
      data2 = file.read()
      file.close()
    with open(f'secondary/{x}.dict', 'w') as file:
      file.write(data2.replace("'", '"'))