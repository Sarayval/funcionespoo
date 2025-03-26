import random

# Realizar función probabilidad
def probabilidad(num_lanzamientos, num_caras):

    # Simular los lanzamientos 
    resultados = [random.choice([0, 1]) for _ in range(num_lanzamientos)]
    
    # Calcular la probabilidad de obtener el número de caras (1)
    prob = resultados.count(1) / num_lanzamientos
    return prob

# Ejemplos de uso 
num_lanzamientos = 10
num_caras = 6  

prob = probabilidad(num_lanzamientos, num_caras)
print(f"La probabilidad de obtener caras en {num_lanzamientos} lanzamientos es {prob:.4f}")
