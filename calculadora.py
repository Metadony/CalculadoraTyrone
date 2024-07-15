# Calculadora

#Operaçoes
op = int(input(' Digite o numero correspondente a operaçao que deseja \n\n 1. Soma \n 2. Subtraçao \n 3. Multiplicaçao \n 4. Divisao \n 5. Para encerrar \n'))
while op > 5:
 op = int(input('\n Digite um numero valido \n\n 1. Soma \n 2. Subtraçao \n 3. Multiplicaçao \n 4. Divisao \n 5. Para encerrar \n'))

while op < 5:

  #Escolha os valores
  num1 = int(input('\nIntroduza o primeiro valor: '))
  num2 = int(input('Introduza o segundo valor: '))

  #Operaçoes basicas
  if op == 1:
    resultado = num1 + num2
    print('\n O resultado é:',resultado)
  elif op == 2:
    resultado = num1 - num2
    print('\n O resultado é:',resultado)
  elif op == 3:
    resultado = num1 * num2
    print('\n O resultado é:',resultado)
  elif op == 4:
    if num2 == 0:
      print('\n Nao é possivel dividir')
    else:
      resultado = num1 / num2
      print('\n O resultado é:',resultado)

#Looping
  print('\n ------------------------- \n')
  op = int(input(' Digite o numero correspondente a operaçao que deseja \n\n 1. Soma \n 2. Subtraçao \n 3. Multiplicaçao \n 4. Divisao \n 5. Para encerrar \n'))
while op > 5:
 op = int(input('\n Digite um numero valido \n\n 1. Soma \n 2. Subtraçao \n 3. Multiplicaçao \n 4. Divisao \n 5. Para encerrar \n'))

