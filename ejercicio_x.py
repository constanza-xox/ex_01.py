'''contador = 1
numero_input = int(input("Ingrese numero: "))
fact = 1
while contador < numero_input:

  contador = contador + 1 # se agrega una unidad hasta llegar al numero-input
  fact =  fact * contador
  print("contador: ",contador)
  print(fact)
  # contador += 1
print("El factorial de",numero_input,"es:",fact)'''


'''hasta_variable_final = 0
resta = 0
while hasta_variable_final < 5:
  hasta_variable_final = hasta_variable_final + 1
  num_posi= int(input("ingrese un numero positivo: "))
  resta = resta - hasta_variable_final
print("La resta es:",resta)  
'''


variable_3= 0
variable_2 = 0
variable= 0
while variable < 5: 
  num= int(input("ingrese un numero entero ;3  : " ))
  variable= variable+1 
  if num > 0:
    variable_2=variable_2+1
  if num % 2==0:
    variable_3= variable_3 + 1
  
print(f"los numeros mayores a son: {variable_2}")
print(f"los numeros pares son: {variable_3}")
