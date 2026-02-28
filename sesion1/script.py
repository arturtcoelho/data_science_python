articulos = [{"nombre": "rueda", "precio": 20}, {"nombre": "puerta", "precio": 15}]

ventas = [{"articulo": "rueda", "cliente": "ruben"}]

articulos_formateados = {a["nombre"]:a["precio"] for a in articulos}
ventas_formateados = {a["cliente"]:a["articulo"] for a in ventas}

print(articulos_formateados)

print(articulos_formateados[ventas_formateados["ruben"]])