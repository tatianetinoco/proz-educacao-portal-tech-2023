#Imprimir um número para cada andar de um hotel de 20 andares exceto o número 13. 
#Imprima em ordem decrescente (20, 19, 18...)


for n in range(20, 0, -1):
 if (n == 13):
  continue
 print(n," Andar", sep = "°")
print("Fim") 


print("\n")


n = 21
while (n > 1):
 n -= 1
 if (n == 13):
  continue
 print(n," Andar", sep = "°")
print("Fim") 
