import random

# Definindo os elementos das listas "basic" e "adv"
# Uma boa opção seria manter apenas primeiro e segundo nome dos elementos
basic = ['Adriel Faustino de Oliveira',
'Amanda Emi Yamasaki',
'Ana Werneck de Souza Dias',
'Felipe de Souza Lourenço',
'Fernanda Mayumi Sakamoto Iizuka',
'Guilherme Vinicius Afonso Dias de Freitas',
'Kim Ju Hyang',
'Leticia Amy Siramidu',
'Marcelo Tamay Honda',
'Maria Dulce Navarro de Britto Matos',
'Mateus Pamio Forcione de Oliveira e Souza',
'Milena da Silva Ramos',
'Paulo Sergio Almeida de Oliveira',
'Theo Borten Radesca Migliano',
'Vitor Tatiama Gouveia']

adv = ['André Menniti Pennini',
'Fernanda Mees Antunes',
'Gabriel Grub Vidal da Silva',
'Henrique Nogueira Pedro Lindoso']

# Embaralha a lista "basic" e separa seus elementos em novas listas (grupos)
random.shuffle(basic)

g1 = basic[:4]
g2 = basic[4:8]
g3 = basic[8:12]
g4 = basic[12:15]

# Embaralha a lista "adv" e adiciona seus elementos de um em um aos grupos
random.shuffle(adv)

g1.append(adv[0])
g2.append(adv[1])
g3.append(adv[2])
g4.append(adv[3])

# Imprime os elementos dos grupos
print(f'Grupo 1: {g1}\n')
print(f'Grupo 2: {g2}\n')
print(f'Grupo 3: {g3}\n')
print(f'Grupo 4: {g4}\n')

# Tentei fazer de uma forma mais bonitinha e falhei (╥﹏╥)
# De qualquer forma deixarei aqui para teste futuro
'''
print(f"✨Grupo 1✨:{' / '.join(g1)}\n")
print(f"✨Grupo 2✨:{' / '.join(g2)}\n")
print(f"✨Grupo 3✨:{' / '.join(g3)}\n")
print(f"✨Grupo 4✨:{' / '.join(g4)}\n")
'''
