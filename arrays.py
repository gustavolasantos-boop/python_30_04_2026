lista_frutas = ["Banana ," , "Maça", "Morango" ]

# lista_frutas[0] = "Banana"
# lista_frutas[1] = "maça"
# lista_frutas[2] = "Morango"


print(lista_frutas[0])

lista_frutas.append("Pera")
print(lista_frutas)

qtd_frutas = len(lista_frutas)
print("Qtd de frutas: ", qtd_frutas)

# FOR INDEXADO PARA PERCORRER

for i in range(qtd_frutas):
    print(lista_frutas[i])

# FOR EAC em python
for fruta in lista_frutas:
    print(fruta)