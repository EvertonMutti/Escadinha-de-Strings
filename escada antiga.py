#%%
nome = input('Digite um nome para soletrar:') 
s=""
for letra in nome:
  s=s+letra
  for l in range(len(nome)):
    h = s[0:8-l]
    print(h)
#%%
nome = input('Digite um nome para soletrar:') 
nome2=nome
for (c, letra) in enumerate(nome):
  nome2=nome+letra
for l in range(len(nome)):
    h = nome2[0:-1-l]
    print(h)
