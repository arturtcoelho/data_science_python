print("Rectangulo: 1")
print("Circulo: 2")
print("Triangulo: 3")
forma = int(input("Elije tu forma: "))

def calcula_forma():
    try:
        if forma == 1: # rectangulo
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            if base < 0 or altura < 0:
                raise Exception("Valor negativo")
            area = base * altura
            perimetro = base*2 + altura*2
            return area, perimetro
        elif forma == 2: # circulo
            radius = float(input("radius: "))
            if radius < 0:
                raise Exception("Valor negativo")
            area = 3.1415 * radius**2
            perimetro = 3.1415 * radius*2
            return area, perimetro
        elif forma == 3: # triangulo
            base = float(input("Base: "))
            altura = float(input("Altura: "))
            if base < 0 or altura < 0:
                raise Exception("Valor negativo")
            area = (base * altura) / 2
            perimetro = (base**2 + altura**2)**(1/2) + base + altura
            return area, perimetro
        else:
            print("Forma invalida")
    except ValueError:
        print("Por favor escribe un numero")
    except Exception:
        print("Paso un error no especificado")
    return None, None

area, perimetro = 0, 0
while not area and not perimetro:
    area, perimetro = calcula_forma()

print(f"Area: {area}")
print(f"Perimetro: {perimetro}")
