'''
Práctica Return 1
Crea una función llamada potencia que tome dos valores numéricos como argumentos. 
Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, y el segundo como exponente:
'''
def potencia(base, exponente):
    total = base**exponente
    print(total)
    return total
potencia(3,4)