with open('union.txt', 'r') as f1, open('consulta.txt', 'r') as f2, open('comentarios.txt', 'r') as f3:
    # Leemos todas las líneas de cada archivo y las guardamos en las variables l1, l2 y l3
    l1 = f1.readlines()
    l2 = f2.readlines()
    l3 = f3.readlines()

# Abrimos el archivo resultado.txt en modo escritura
with open('resultado.txt', 'w') as f:
    # Recorremos cada una de las líneas de cada archivo
    for line1 in l1:
        for line2 in l2:
            for line3 in l3:
                # Escribimos en el archivo resultado.txt la línea del archivo union.txt, seguida de un espacio y la línea del archivo consulta.txt, seguida de otro espacio y la línea del archivo comentarios.txt
                f.write(line1.strip() + ' ' + line2.strip() + ' ' + line3.strip() + '\n')

# Abrimos el archivo resultado.txt en modo lectura y el archivo espacios.txt en modo lectura
with open('resultado.txt', 'r') as f1, open('espacios.txt', 'r') as f2:
    # Leemos todas las líneas de cada archivo y las guardamos en las variables l1 y l2
    l1 = f1.readlines()
    l2 = f2.readlines()

# Abrimos el archivo resultadofinal.txt en modo escritura
with open('resultadofinal.txt', 'w') as f:
    # Escribimos en el archivo resultadofinal.txt las líneas de resultado.txt sin modificar
    f.writelines(l1)
    # Recorremos cada una de las líneas de resultado.txt
    for line1 in l1:
        # Recorremos cada una de las líneas de espacios.txt
        for line2 in l2:
            # Reemplazamos todos los espacios en la línea de resultado.txt por la línea de espacios.txt
            new_line = line1.replace(' ', line2.strip())
            # Escribimos en el archivo resultadofinal.txt la línea modificada
            f.write(new_line)

def generar_combinaciones(linea):
    combinaciones = []
    for i in range(len(linea)):
        # Si es una letra, generamos las combinaciones
        if linea[i].isalpha():
            # Si es mayúscula, añadimos la minúscula
            if linea[i].isupper():
                combinacion = linea[:i] + linea[i].lower() + linea[i+1:]
                combinaciones.append(combinacion)
            # Si es minúscula, añadimos la mayúscula
            else:
                combinacion = linea[:i] + linea[i].upper() + linea[i+1:]
                combinaciones.append(combinacion)
    return combinaciones

# Abrimos el archivo resultadofinal.txt
with open("resultadofinal.txt", "r") as f:
    # Abrimos el archivo resultadofinalcombinaciones.txt en modo escritura
    with open("resultadofinalcombinaciones.txt", "w") as f_comb:
        # Leemos línea a línea el archivo resultadofinal.txt
        for linea in f:
            # Generamos las combinaciones de la línea
            combinaciones = generar_combinaciones(linea)
            # Añadimos la línea original al archivo resultadofinalcombinaciones.txt
            f_comb.write(linea)
            # Añadimos todas las combinaciones al archivo resultadofinalcombinaciones.txt
            for combinacion in combinaciones:
                f_comb.write(combinacion)

import urllib.parse

# Abrimos el archivo resultadofinal.txt en modo lectura
with open("resultadofinalcombinaciones.txt", "r") as f:
    # Leemos todas las líneas del archivo
    lines = f.readlines()

# Abrimos el archivo resultadofinalurlencodeado.txt en modo escritura
with open("resultadofinalurlencodeado.txt", "w") as f:
    # Primero escribimos todas las líneas sin realizar cambios
    f.writelines(lines)
    # Añadimos una línea en blanco para separar las líneas originales de las líneas codificadas
    f.write("\n")

    # Realizamos la codificación de cada línea
    for line in lines:
        # Urlencode
        encoded_line = urllib.parse.quote(line)
        f.write(encoded_line)
        # Añadimos una línea en blanco para separar las líneas codificadas
        f.write("\n")

        # Doble urlencode
        double_encoded_line = urllib.parse.quote_plus(line)
        f.write(double_encoded_line)
        # Añadimos una línea en blanco para separar las líneas codificadas
        f.write("\n")

import os

try:
    # Elimina el archivo resultadofinal.txt
    os.remove("resultadofinal.txt")
    os.remove("resultado.txt")
    os.remove("resultadofinalcombinaciones.txt")
    os.rename("resultadofinalurlencodeado.txt", "diccionarioallcombinations.txt")
except FileNotFoundError:
    # Archivo no encontrado, no hacer nada
    pass