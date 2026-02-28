import json

with open("datas.json", 'r') as f:
    string_datos = f.read()

print(string_datos)

objeto_python = json.loads(string_datos)
print(objeto_python)
