from database.mysqldb import conexion


def mostrarInstrumentos():
    try:
        cursor_mysql = conexion.cursor()
        cursor_mysql.execute("SELECT * FROM instruments;")

        for inst in cursor_mysql:
            print(inst)

        cursor_mysql.close()
    except Exception as ex:
        print(ex)

    finally:
        conexion.close()


def buscarInstrumentoPorID(idInstrumento):
    try:
        cursor_mysql = conexion.cursor()

        tuplaArgumentos = (idInstrumento,)

        queryBusquedaPorID = "SELECT * FROM instruments WHERE id = %s"

        cursor_mysql.execute(queryBusquedaPorID, tuplaArgumentos)

        for inst in cursor_mysql:
            print(inst)

        cursor_mysql.close()
    except Exception as ex:
        print(ex)

    finally:
        conexion.close()


def buscarInstrumentoPorNombre(nombreInstrumento):
    try:
        cursor_mysql = conexion.cursor()

        # tupla = (nombreInstrumento, nombreInstrumento, nombreInstrumento)

        queryBusquedaPorNombre = "SELECT * FROM instruments WHERE instrumento LIKE '%" + nombreInstrumento + "%' " \
                                 "OR instrumento LIKE '%" + nombreInstrumento + "' " \
                                 "OR instrumento LIKE '" + nombreInstrumento + "%'; "

        # consulta = "SELECT * FROM instruments WHERE instrumento LIKE %%s% " \
        #            "OR instrumento LIKE %%s " \
        #            "OR instrumento LIKE %s% "

        cursor_mysql.execute(queryBusquedaPorNombre)

        for inst in cursor_mysql:
            print(inst)

        cursor_mysql.close()
    except Exception as ex:
        print(ex)

    finally:
        conexion.close()


def insertarInstrumento(instrumento):
    try:
        cursor_mysql = conexion.cursor()

        queryInsert = "INSERT INTO instruments (instrumento, marca, modelo, imagen, precio, costoEnvio, " \
                      "cantidadVendida, descripcion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"

        tuplaArgumentos = (instrumento.nombre, instrumento.marca, instrumento.modelo, instrumento.imagen,
                           instrumento.precio, instrumento.costoEnvio, instrumento.cantidadVendida,
                           instrumento.descripcion)

        cursor_mysql.execute(queryInsert, tuplaArgumentos)

        conexion.commit()

        cursor_mysql.close()

        print(instrumento.nombre + " insertado/a existosamente!")
    except Exception as ex:
        print(ex)
    finally:
        conexion.close()


def deleteInstrumento(idInstrumento):
    try:
        cursor_mysql = conexion.cursor()

        tuplaArgumentos = (idInstrumento,)

        queryDelete = "DELETE FROM instruments WHERE id = %s"

        cursor_mysql.execute(queryDelete, tuplaArgumentos)

        conexion.commit()

        cursor_mysql.close()

    except Exception as ex:
        print(ex)
    finally:
        conexion.close()


def updateNombreInstrumento(idInstrumento, nuevoNombreInstrumento):
    try:
        cursor_mysql = conexion.cursor()

        tuplaArgumentos = (nuevoNombreInstrumento, idInstrumento)

        queryUpdateName = "UPDATE instruments SET instrumento = %s WHERE id = %s ;"

        cursor_mysql.execute(queryUpdateName, tuplaArgumentos)

        conexion.commit()

        cursor_mysql.close()

        print("Instrumento de id " + str(idInstrumento) + " cambiado existosamente!")
    except Exception as ex:
        print(ex)
    finally:
        conexion.close()


# deleteInstrumento(9)
# nuevoInstrumento = Instrumento("Kalimba", "Kimbra", "2011", "Kalimba.png", 15000.38, "G", 10,
#  "La Kalimba de Kimbra usada en el video 'Somebody that I used to know' Yada Yada.")
# insertarInstrumento(nuevoInstrumento)

# busqueda = input("Busque un instrumento por nombre: ")
# buscarInstrumentoPorNombre(busqueda)
# updateNombreInstrumento(10, "Kalimba Musical de 10 notas")
