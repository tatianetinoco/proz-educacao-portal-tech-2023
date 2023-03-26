#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2023. 
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou
#ou completará, no ano atual.

#Caso o usuário não digite um número ou apareça um inválido no campo do ano, 
#o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.


resposta = False
while (resposta == False):
  print("Informe o seu primeiro nome: ")
  try:
    primeiroNome = input()
    if all(c.isalpha() or c.isspace() for c in primeiroNome):
        resposta = True
    else:
        print("Ocorreu Erro! Digite um Nome Válido")
  except:
    print("Informe um nome válido (somente letras)")


resposta = False
while (resposta == False):
 print("Informe o seu sobrenome: ")
 try:
    sobrenome = input()
    if all(c.isalpha() or c.isspace() for c in sobrenome):
      resposta = True
    else:
      print("Ocorreu Erro! Digite um Nome Válido")
 except:
    print("Informe um nome válido (somente letras)")


resposta = False
while (resposta == False):
  print("Informe o dia de seu nascimento: ")
  try:
    diaNasc = int(input())
    if int(diaNasc) < 1 or int(diaNasc) > 31:
      print("Informe um Dia válido (1 - 31):")
    else:
     resposta = True
  except:
    print("ERRO .. Digite Novamente!! Válido somente números")


resposta = False
while (resposta == False):
  print("Informe o mês de seu nascimento: ")
  try:
    mesNasc = int(input())
    if int(mesNasc) < 1 or int(mesNasc) > 12:
      print("Informe um Mês válido (1 - 12):")
    else:
     resposta = True
  except:
    print("ERRO .. Digite Novamente!! Válido somente números")
    

resposta = False
while (resposta == False):
  print("Informe o Ano de seu nascimento: ")
  try:
    anoNasc = int(input())
    if int(anoNasc) < 1922 or int(anoNasc) > 2023:
      print("Informe um Ano válido (1922 - 2023):")
    else:
     resposta = True
  except:
    print("ERRO .. Digite Novamente!! Válido somente números")   
    

resposta = False
while (resposta == False):
  print("Informe o Dia atual: ")
  try:
    diaAtual = int(input())
    if int(diaAtual) < 1 or int(diaAtual) > 31:
      print("Informe um Dia válido (1 - 31):")
    else:
     resposta = True
  except:
    print("ERRO .. Digite Novamente!! Válido somente números")    


resposta = False
while (resposta == False):
  print("Informe o Mês atual: ")
  try:
    mesAtual = int(input())
    if int(mesAtual) < 1 or int(mesAtual) > 12:
      print("Informe um Mês válido (1 - 12):")
    else:
     resposta = True
  except:
    print("ERRO .. Digite Novamente!! Válido somente números")    


resposta = False
while (resposta == False):
  print("Informe o Ano atual: ")
  try:
    anoAtual = int(input())
    if int(anoAtual) != 2023:
      print("Digite o Ano Atual válido:")
    else:
     resposta = True
  except:
    print("ERRO .. Digite Novamente!! Válido somente números")    

 
nome = primeiroNome.capitalize() + " " + sobrenome.capitalize()
idade = int(anoAtual) - int(anoNasc)
print("-="*25)
print("Nome Completo:",nome)
print("Data Nascimento: " + str(diaNasc), str(mesNasc), str(anoNasc) , sep = "/")
  
if int(mesNasc) > int(mesAtual) or (int(mesNasc) == int(mesAtual) and int(diaNasc) > int(diaAtual) ):
   idade = idade - 1
   print("Olá",primeiroNome.capitalize(),", Você Ainda Não Fez Aniversário Esse Ano.") 
else:
   print("Parabéns,",primeiroNome.capitalize(),"! Você Já Fez Aniversário Esse Ano.")

print("Você tem",idade, "Anos!!")  
print("-="*25) 
