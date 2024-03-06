import os
#class criada para organizar os comandos do programa fibonacci! :D 
class FIB:
  def CalculoProx(self, valor1, valor2):
   return anteriores[-1] + anteriores[-2]
  
  def CalculoFib(self, num1):
   anteriores = []
   valor1 = 0
   valor2 = 1
   while (valor2<num1):
    anteriores.append(valor1)
    valor1, valor2 = valor2, valor1 + valor2
   return anteriores
  
  def NumerosNFib(self, n):
    return int(n ** 0.5) ** 2 == n

  def NumerosFib(self, num):
    return self.NumerosNFib(5 * num ** 2 + 4) or self.NumerosNFib(5 * num ** 2 - 4)

MENU1 = {'SOMA','soma','1'}
MENU2 = {'FIBONACCI','fibonacci','2'}
MENU3 = {'INVERTER','inverter','3'}
menu = input('Escolha qual programa deseja iniciar\n''\n1 = SOMA''\n2 = FIBONACCI''\n3 = INVERTER\n')

#enquanto para fazer um loop na hora de escolher o programa.
while(menu not in MENU1 and menu not in MENU2 and menu not in MENU3):
  menu = input('Escolha apenas o numero ou nome correto...')
  os.system('cls')
  os.system('clear')
  
#comando para SOMAR seguindo a pergunta sem utilizar nenhum meio de entrada GUPY R=91
if (menu in MENU1):
  print('Iniciando Programa SOMA...')
  indice = 13 
  SOMA = 0 
  K = 0
  while(K<indice):
    K = K + 1
    SOMA = SOMA + K
    print('Valor: {}'.format(SOMA))
  

#comando para Calcular e informar os antecessores e o proximo numero na sequencia de fibonacci
elif (menu in MENU2):
  print('Iniciando Programa FIBONACCI...')
  Num = int(input('Digite um numero: '))
  Init = FIB()
  anteriores= Init.CalculoFib(Num)
  valor2= Init.CalculoFib(Num)
  valor1= Init.CalculoFib(Num)
  #Informa o numero escolhido como correto, informa os anteriores e o proximo numero
  if (Init.NumerosFib(Num)):
    print('O numero informado faz parte da sequencia de fibonacci!!! \nOs antecessores a {} sao :{} \nO numero Proximo ao escolhido e: '.format(Num, anteriores),Init.CalculoProx(valor1, valor2))
   #Else utilizado para informar que nao existe o numero informado no fibonacci e informa o numero que esta mais proximo 
  else:
      print('O numero informado nao faz parte da sequencia de fibonacci!!!! \nOs numeros que fazem parte anteriores ao escolhido sao: ',anteriores)
      print('O numero Proximo ao escolhido e: ', Init.CalculoProx(valor1, valor2))


#comando para inverter a STR utilizando [::-1] ou um fatiamento fazendo o programa percorrer a STR de tras pra frente usando o -1
elif (menu in MENU3):
  print('Iniciando Programa INVERTER')
  Normal = str(input('Escreva algo para que possa inverter: '))
  Inverter = Normal[::-1]
  print('Assim fica estranho... ', Inverter)
  
