
'''listarCategorias: El método recibe una lista con todas las categorías y las listará
como se muestra en las capturas de más adelante.'''
def listarCategorias(lista_categorías):
    print("*** BIENVENIDO AL PROGRAMA PRODUCTOS INFORMATICA ********")
    print("Se procede a cargar las categorías de los productos...")
    print("")
    print("Categorias disponibles:")
    for i in range(len(lista_categorías)):
        print(i + ".  " + lista_categorías[i][0])


'''verificarEleccionCategoria: El método debe encargarse de recibir la cantidad de
categorías disponibles y preguntar al usuario que introduzca un número válido y
permitido según la cantidad de categorías.'''
def verificarEleccionCategoria(max_categorias):
    while True:
        num = input("Introduce un número entre 0 " + (max_categorias - 1))
        num = int(num)
        if num >= 0 and num < max_categorias:
            return num




'''mostrarProductosCategoria: El método recibirá una lista con los datos de los productos
de dicha categoría y la categoría seleccionada los mostrará por pantalla.'''
def mostrarProductosCategoria(lista_categorias, num_categoria):
    print("******** LISTADO PRODUCTOS DE " + lista_categorias[num_categoria][0] + " ********")
    print("******** LISTADO PRODUCTOS DE %s ********", lista_categorias[num_categoria][0])
    # Pintar noms de productes a categoria num_categoria
    for i in range(len(lista_categorias[num_categoria][1])):
        print(str(i) + "." + lista_categorias[num_categoria][1][i][0])

    print("-------------------------------------")

    # contar productos C-style
    contador = 0
    for i in range(len(lista_categorias[num_categoria][1])):
        contador += 1

    # Media precio productos C-style
    sum = 0
    for i in range(len(lista_categorias[num_categoria][1])):
        sum += lista_categorias[num_categoria][1][i][1]

    median = sum / float(contador)

    print("Total productos: " + str(contador))
    print("Precio medio: " + str(median))

def indexCategoryInData(category_name, data):
    for i in range(len(data)):
        if data[i][0] == category_name:
            return i
    return -1

data = []
f = open("../productosInformatica.txt")
for line in f.readlines():
    name = line.split(",")[0].rstrip(" ")
    category = line.split(",")[1].lstrip(" ")
    price = float(line.split(",")[2].rstrip("\n").lstrip(" "))

    category_index = indexCategoryInData(category, data)
    # category not present, we need to create the data for the category
    if category_index == -1:
        category_data = []
        category_data.append(category)
        products = []
        read_product = []
        read_product.append(name)
        read_product.append(price)
        products.append(read_product)
        category_data.append(products)
        data.append(category_data)

    else:  # category present, append product
        read_product = []
        read_product.append(name)
        read_product.append(price)
        data[category_index][1].append(read_product)


print(data)
mostrarProductosCategoria(data, 3)


# [dades_categoria1, dades_categoria2, ... , dades_categorian] amn tantas posicions com categorias
# Dins de cada pos de la llista hi ha les dades de cada categoria
# dades_categoria = [Nom, [dades_de_productes_que_pertanyen_a_categoria1, dades_de_productes_que_pertanyen_a_categoria2, ...]]
# dades_producte = [Nom, preu]

'''[[nom_categoria1, dades_categoria1], [nom2, dades_categoria2], ...  ] =
[[nom_categoria1, [dades_producte1, dades_producte2, ...]], [nom_categoria2, dades_producte1, dades_producte2, ...], ...  ] =
[[nom_categoria1, [[Nom_producte1, preu_prioducte1], [Nom_producte1, preu_prioducte1], ...]], [nom_categoria2, [Nom_producte3, preu_prioducte3], [Nom_producte4, preu_prioducte4],...  ...], ...  ] =


dades[n][1][p][1]
'''