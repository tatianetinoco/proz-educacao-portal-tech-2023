#Faça uma função calculadora que os números e as operações serão feitas pelo usuário. 
#O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. 
#No início, o programa mostrará a seguinte lista de operações:

#1: Soma
#2: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair

#Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, 
#o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.
#Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada.
#Depois precisa executar a operação e mostrar o resultado na tela. 
#Quando o usuário escolher a opção “Sair”, o sistema irá parar.
#É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado.


def adicao():
 return num1+num2

def multiplicacao():
 return num1*num2

def subtracao():
 return num1-num2

def divisao():
 return num1/num2

escolha = False
while (escolha == False):
   print("\n")
   print("1. Adição")
   print("2. Subtração")
   print("3. Multiplicação")
   print("4. Divisão")
   print("0. Sair")
   operacao = float(input("Escolha qual operação deseja realizar (1, 2, 3, 4 ou 0): "))

   if operacao==1:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("O Resultado da Soma: ",num1, "+",num2, "=",adicao())

   elif operacao==2:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("O Resultado da Subtração: ",num1, "-",num2, "=",subtracao())

   elif operacao==3:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("O Resultado da Multiplicação: ",num1, "*",num2, "=",multiplicacao())

   elif operacao==4:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    print("O Resultado da Divisão: ",num1, "/",num2, "=",divisao())

   elif operacao==0:
    print("\n")
    print("Fim de operação")
    escolha = True
   else:
    print("\n")
    print("Essa opção não existe! Escolha um número Válido.")