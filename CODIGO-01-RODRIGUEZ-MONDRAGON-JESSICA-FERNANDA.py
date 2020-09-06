from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

admin = [['CEO', 'ceolfs'], ['Operaciones', 'oplfs'], ['ventas', 'venlfs'],
         ['marketing', 'mktlfs'],  ['finanzas', 'finlfs']]

usuario = input('Introduce tu usuario: ')
paswd = input('Ingresa tu contraseña: ')

adm = 0
for i in admin:
    if i[0] == usuario and i[1] == paswd:
        adm = 1

if adm == 1:
    print('\nBienvenido a lifestore\n')
    salir = False
    opcion = 0

    while not salir:
        print('\n¿Qué deseas consultar?\n')

        print('1. Productos con mayores ventas')
        print('2. Productos con mayores búsquedas')
        print("3. Productos con menores ventas por categoría")
        print("4. Productos con menores búsquedas por categoría")
        print("5. Productos con mejores reseñas")
        print('6. Productos con peores reseñas')
        print('7. Ventas totales mensuales')
        print('8. Ingresos totales mensuales')
        print('9. Meses con mayores ventas')
        print('10. Salir')

        opcion = input('\nElige una opción: ')

        if opcion == '1':
            print("Opcion 1: \nProductos con mayores ventas\n")
            print(
                'A continuación se encuentran los 50 productos con mayores ventas'
            )
            c = 0
            ventas = []
            for p in lifestore_products:
                for v in lifestore_sales:
                    if p[0] == v[1]:
                        c += 1
                form = [p[0], p[1], c]
                ventas.append(form)
                c = 0

            def ordenar(valor):
                return valor[2]

            ventas2 = sorted(ventas, key=ordenar, reverse=True)
            for t in ventas2[:50]:
                print('El producto: ', t[1], 'se vendió: ', t[2], 'veces \n')

        elif opcion == '2':
            print('\nLos 100 productos con mayores búsquedas son: \n')
            t = 0
            busqueda = []
            for p in lifestore_products:
                for s in lifestore_searches:
                    if p[0] == s[1]:
                        t += 1
                formato = [p[0], p[1], t]
                busqueda.append(formato)
                t = 0

            def ordenar(valor):
                return valor[2]

            for t in sorted(busqueda, key=ordenar, reverse=True):
                print('El producto: ', t[1], 'con ID: ', t[0], ',se buscó: ',
                      t[2], 'veces \n')

        elif opcion == '3':
            exit = False
            suboption = 0
            while not exit:
                print('\n¿Qué categoría deseas consultar?\n')
                print('a. Procesadores')
                print('b. Tarjetas de video')
                print('c. Tarjetas madre')
                print('d. Discos duros')
                print('e. Memorias USB')
                print('f. Pantallas')
                print('g. Bocinas')
                print('h. Aufifonos')
                print('i. Todas las categorías')
                print('s. Regresar al menú principal')

                suboption = input('\nElige una opción: ')

                if suboption == 'a':
                    print('\nVentas de procesadores\n')
                    cat = 0
                    categoria = []

                    for p in lifestore_products:
                        for s in lifestore_sales:
                            if p[0] == s[1]:
                                cat += 1
                        formato = [p[3], p[1], cat]
                        categoria.append(formato)
                        cat = 0

                    a = [y for y in categoria if y[0] == 'procesadores']

                    def ordenar(valor):
                        return valor[2]

                    for t in sorted(a, key=ordenar, reverse=False):
                        print('CATEGORIA:', t[0], ';El producto: ', t[1],
                              'se vendió: ', t[2], 'veces \n')
                elif suboption == 'b':
                    print('\n Ventas de Tarjetas de video \n')

                    cat = 0
                    categoria = []

                    for p in lifestore_products:
                        for s in lifestore_sales:
                            if p[0] == s[1]:
                                cat += 1
                        formato = [p[3], p[1], cat]
                        categoria.append(formato)
                        cat = 0
                    b = [y for y in categoria if y[0] == 'tarjetas de video']

                    def ordenar(valor):
                        return valor[2]

                    for t in sorted(b, key=ordenar, reverse=False):
                        print('CATEGORIA:', t[0], ';El producto: ', t[1],
                              'se vendió: ', t[2], 'veces \n')

                elif suboption == 'c':
                    print('\n Ventas de Tarjetas madre \n')
                    cat = 0
                    categoria = []

                    for p in lifestore_products:
                        for s in lifestore_sales:
                            if p[0] == s[1]:
                                cat += 1
                        formato = [p[3], p[1], cat]
                        categoria.append(formato)
                        cat = 0
                    c = [y for y in categoria if y[0] == 'tarjetas madre']

                    def ordenar(valor):
                        return valor[2]

                    for t in sorted(c, key=ordenar, reverse=False):
                        print('CATEGORIA:', t[0], ';El producto: ', t[1],
                              'se vendió: ', t[2], 'veces \n')

                elif suboption == 'd':

                    print('\n Ventas de Discos duros \n')
                    cat = 0
                    categoria = []

                    for p in lifestore_products:
                        for s in lifestore_sales:
                            if p[0] == s[1]:
                                cat += 1
                        formato = [p[3], p[1], cat]
                        categoria.append(formato)
                        cat = 0
                    d = [y for y in categoria if y[0] == 'discos duros']

                    def ordenar(valor):
                        return valor[2]

                    for t in sorted(d, key=ordenar, reverse=False):
                        print('CATEGORIA:', t[0], ';El producto: ', t[1],
                              'se vendió: ', t[2], 'veces \n')

                elif suboption == 'e':
                    print('\n Ventas de Memorias USB \n')
                    cat = 0
                    categoria = []

                    for p in lifestore_products:
                        for s in lifestore_sales:
                            if p[0] == s[1]:
                                cat += 1
                        formato = [p[3], p[1], cat]
                        categoria.append(formato)
                        cat = 0
                    e = [y for y in categoria if y[0] == 'memorias usb']

                    def ordenar(valor):
                        return valor[2]

                    for t in sorted(e, key=ordenar, reverse=False):
                        print('CATEGORIA:', t[0], ';El producto: ', t[1],
                              'se vendió: ', t[2], 'veces \n')

                elif suboption == 'f':
                    print('\n Ventas de Pantallas \n')
                    cat = 0
                    categoria = []

                    for p in lifestore_products:
                        for s in lifestore_sales:
                            if p[0] == s[1]:
                                cat += 1
                        formato = [p[3], p[1], cat]
                        categoria.append(formato)
                        cat = 0
                    f = [y for y in categoria if y[0] == 'pantallas']

                    def ordenar(valor):
                        return valor[2]

                    for t in sorted(f, key=ordenar, reverse=False):
                        print('CATEGORIA:', t[0], ';El producto: ', t[1],
                              'se vendió: ', t[2], 'veces \n')

                elif suboption == 'g':
                    print('\n Ventas de Bocinas \n')
                    cat = 0
                    categoria = []

                    for p in lifestore_products:
                        for s in lifestore_sales:
                            if p[0] == s[1]:
                                cat += 1
                        formato = [p[3], p[1], cat]
                        categoria.append(formato)
                        cat = 0
                    g = [y for y in categoria if y[0] == 'bocinas']

                    def ordenar(valor):
                        return valor[2]

                    for t in sorted(g, key=ordenar, reverse=False):
                        print('CATEGORIA:', t[0], ';El producto: ', t[1],
                              'se vendió: ', t[2], 'veces \n')

                elif suboption == 'h':
                    print('\n Ventas de Audífonos \n')
                    cat = 0
                    categoria = []

                    for p in lifestore_products:
                        for s in lifestore_sales:
                            if p[0] == s[1]:
                                cat += 1
                        formato = [p[3], p[1], cat]
                        categoria.append(formato)
                        cat = 0
                    h = [y for y in categoria if y[0] == 'audifonos']
                    for t in sorted(h, key=ordenar, reverse=False):
                        print('CATEGORIA:', t[0], ';El producto: ', t[1],
                              'se vendió: ', t[2], 'veces \n')

                elif suboption == 'i':
                    print(
                        '\n Listado de los 50 productos con menores ventas por categoría: \n'
                    )
                    cat = 0
                    categoria = []

                    for p in lifestore_products:
                        for s in lifestore_sales:
                            if p[0] == s[1]:
                                cat += 1
                        formato = [p[3], p[1], cat]
                        categoria.append(formato)
                        cat = 0

                    def ordenar2(valor):
                        return valor[2]

                    categoria2 = sorted(categoria, key=ordenar2, reverse=False)
                    for t in categoria2[:50]:
                        print('CATEGORIA:', t[0], ';El producto: ', t[1],
                              'se vendió: ', t[2], 'veces \n')

                elif suboption == 's':

                    break

                else:
                    print('Opción incorrecta')

        elif opcion == '4':
            print(
                '\n Los 100 productos con menores búsquedas por categoría son los siguientes: \n'
            )
            bus = 0
            categoria_busqueda = []

            for p in lifestore_products:
                for s in lifestore_searches:
                    if p[0] == s[1]:
                        bus += 1
                formato = [p[3], p[1], bus]
                categoria_busqueda.append(formato)
                bus = 0

            def ordenar(valor):
                return valor[2]

            for t in sorted(categoria_busqueda, key=ordenar, reverse=False):
                print('CATEGORIA:', t[0], ';El producto: ', t[1], 'tuvo: ',
                      t[2], 'búsquedas \n')

        elif opcion == '5':
            print(
                '\n Los 20 productos con mejores reseñas, son los siguientes: \n'
            )

            reseña = []
            for p in lifestore_products:
                for s in lifestore_sales:
                    if p[0] == s[1]:
                        formato = [p[1], s[2]]
                reseña.append(formato)

            def res(valor):
                return valor[1]

            mejores_reseñas = sorted(reseña, key=res, reverse=True)
            for t in mejores_reseñas[:20]:
                print('El producto: ', t[0], 'obtuvo una calificación de: ',
                      t[1])

        elif opcion == '6':
            print(
                '\n Los 20 productos con las reseñas mas bajas, son los siguientes: \n'
            )

            reseña_mala = []
            for p in lifestore_products:
                for s in lifestore_sales:
                    if p[0] == s[1]:
                        formato = [p[1], s[2]]
                reseña_mala.append(formato)

            def res(valor):
                return valor[1]

            malas_reseñas = sorted(reseña_mala, key=res, reverse=False)
            for t in malas_reseñas[:20]:
                print('El producto: ', t[0], 'obtuvo una calificación de: ',
                      t[1])
        elif opcion == '7':
            print('\n Ventas totales mensuales:\n')
            dev = [(x[3][3:], x[4]) for x in lifestore_sales if x[4] == 1]
            dates = [x[3] for x in lifestore_sales]
            months = [x[3:] for x in dates]
            ventas_por_mes = list(set(months))
            aux = []
            for a in ventas_por_mes:
                aux.append((a, months.count(a), [x[0] for x in dev].count(a)))

            def mon(valor):
                return valor[0]

            for t in sorted(aux, key=mon):
                print('Fecha: ', t[0], 'ventas: ', t[1], 'devoluciones:', t[2])

        elif opcion == '8':
            print('\nIngresos totales mensuales: \n')
            dev = [(x[3][3:], x[4]) for x in lifestore_sales
                   if x[4] == 1]  #devolución

            dates = [x[3] for x in lifestore_sales]
            months = [x[3:] for x in dates]
            months_ = list(set(months))
            aux = []
            for a in months_:
                aux.append((a, months.count(a), [x[0] for x in dev].count(a)))
            aux2 = [[x[3][3:], x[1], x[4]] for x in lifestore_sales]
            id_price = dict(
                zip([x[0] for x in lifestore_products],
                    [x[2] for x in lifestore_products]))
            id_name = dict(
                zip([x[0] for x in lifestore_products],
                    [x[1] for x in lifestore_products]))

            prices = [[x[0], x[1], x[2], id_price[x[1]]] for x in aux2]

            aux3 = []
            aux4 = []

            for m in months_:
                sells = 0
                for p in prices:
                    if p[0] == m:
                        sells += p[3]
                aux4.append([m, sells])

            def ingresos(valor):
                return valor[1]

            for t in sorted(aux4, key=ingresos, reverse=True):
                print('\n Fecha:', t[0], 'ingresos totales: ', t[1])

        elif opcion == '9':
            print('\n Meses con mayores ventas: \n ')
            dev = [(x[3][3:], x[4]) for x in lifestore_sales if x[4] == 1]
            dates = [x[3] for x in lifestore_sales]
            months = [x[3:] for x in dates]
            ventas_por_mes = list(set(months))
            aux = []
            for a in ventas_por_mes:
                aux.append((a, months.count(a), [x[0] for x in dev].count(a)))

            def mon2(valor):
                return valor[1]

            aux2 = sorted(aux, key=mon2, reverse=True)
            mayores_ventas = [x for x in aux2 if x[1] >= 40]
            for t in mayores_ventas:
                print('Mes: ', t[0], 'ventas', t[1])

        elif opcion == '10':
            break
        else:
            print(
                'Opción incorrecta...\ningresa una nueva opción para continuar'
            )
    print("Sesión cerrada")
else:
    print('Usuario o contraseña invalidos, por favor intente de nuevo')
