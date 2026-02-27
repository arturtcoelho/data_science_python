# Ejercicio 1:

import math

def area_rectangulo(base, altura):
    return base * altura

def perimetro_rectangulo(base, altura):
    return 2 * (base + altura)

def area_circulo(radio):
    return math.pi * radio ** 2

def perimetro_circulo(radio):
    return 2 * math.pi * radio

def area_triangulo_rectangulo(cateto1, cateto2):
    return (cateto1 * cateto2) / 2

def perimetro_triangulo_rectangulo(cateto1, cateto2):
    hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
    return cateto1 + cateto2 + hipotenusa

if __name__ == "__main__":
    print("=== Calculadora de Áreas y Perímetros ===")
    print("1. Rectángulo")
    print("2. Círculo")
    print("3. Triángulo Rectángulo")
    
    try:
        figura = int(input("Seleccione una figura (1-3): "))
        
        if figura == 1:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = area_rectangulo(base, altura)
            perimetro = perimetro_rectangulo(base, altura)
            print(f"Área: {area:.2f}")
            print(f"Perímetro: {perimetro:.2f}")
            
        elif figura == 2:
            radio = float(input("Ingrese el radio del círculo: "))
            area = area_circulo(radio)
            perimetro = perimetro_circulo(radio)
            print(f"Área: {area:.2f}")
            print(f"Circunferencia: {perimetro:.2f}")
            
        elif figura == 3:
            cateto1 = float(input("Ingrese el primer cateto: "))
            cateto2 = float(input("Ingrese el segundo cateto: "))
            area = area_triangulo_rectangulo(cateto1, cateto2)
            perimetro = perimetro_triangulo_rectangulo(cateto1, cateto2)
            print(f"Área: {area:.2f}")
            print(f"Perímetro: {perimetro:.2f}")
            
        else:
            print("Opción no válida")
            
    except ValueError:
        print("Error: Ingrese solo números")
    except Exception as e:
        print(f"Error: {e}")