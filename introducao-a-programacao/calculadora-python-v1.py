#Faça uma função calculadora de dois números com três parâmetros: 
#os dois primeiros serão os números da operação 
# e o terceiro a operação a ser executada. 
#Considere a seguinte definição:
#1. Soma / 2. Subtração / 3. Multiplicação / 4. Divisão
#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(n1,n2,op):  
  if op == 1:
    resultado = n1 + n2
  elif op == 2:
    resultado = n1 - n2
  elif op == 3:
    resultado = n1 * n2
  elif op == 4:
    resultado = n1 / n2
  else:
    resultado = "0"
  return resultado

resSoma = calculadora(20,10,1)
resSub = calculadora(20,10,2)
resMult = calculadora(20,10,3)
resDiv = calculadora(20,10,4)
resInv = calculadora(20,10,5)

print("-"*35)
print("Resultado da Soma:",resSoma)   
print("Resultado da subtração:",resSub)   
print("Resultado da multiplicação:",resMult)   
print("Resultado da divisão:",resDiv)   
print("Resultado de operação Inválida:",resInv) 
print("-"*35)