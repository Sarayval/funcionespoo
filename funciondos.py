import random

# Realizar función probabilidad

def probabilidad(num_lanzamientos,num_caras):

#Simular los lanzamientos 
resultados=[random.choice([0,1])] for _ in range(num_lanzamientos)

#Calcular la probabilidad de obtener el número caras
prob=resultados.count(1)/num_lanzamientos
return prob

#Ejemplos de uso (Declaración de objetos)
num_lanzamientos=10
num_caras=6

prob=probabilidad(num_lanzamientos,num_caras)
print (f "la probabilidad de obtener {num_lanzamientos} es {prob:4f}")