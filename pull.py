def pullPrimary(lang): 
  with open(f'primary/{lang}.dict', 'r') as file: return(file.readlines()[0])
def pullSecondary(lang): 
  with open(f'secondary/{lang}.dict', 'r') as file: return(file.readlines()[0])