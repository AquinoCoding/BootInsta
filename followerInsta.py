from datetime import datetime
import instaloader

acesso = instaloader.Instaloader()
acesso.login('******','*****')

seguidores = instaloader.Profile.from_username(acesso.context, 'dwatchpro').get_followers()
seguindo = instaloader.Profile.from_username(acesso.context, 'dwatchpro').get_followees()

print('\n')

print('Seguidores: ' + str(seguidores._data['count']))

print('\n')
      
valor = seguidores._data['edges']
valorII = seguindo._data['edges']

print(f'\nSeguidores\n')

for i in range(len(valor)):
    print(f"{valor[i]['node']['username']}")

print(f'\nSeguindo\n')
          
for i in range(len(valorII)):
    print(f"{(valorII[i]['node']['username'])}")


