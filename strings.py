string = "PaLavrA"

print(string.lower())
print(string.upper())
print(string.title())


 ## interpolação de variaveis

#format
print(f"Essa frase contem pelo menos uma {string.lower()}", end= ".")

#Strings de multiplas linhas

frase_grande = f"""
Coloca a string entre 3
conjuntos de aspas
e deixa quantas linhas quiser
       ou espaços"""

print(frase_grande)

