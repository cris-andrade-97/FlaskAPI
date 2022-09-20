from bson import ObjectId
from database.db import collectionInstrumentos


def getAllInstruments():
    try:
        return collectionInstrumentos().find()
    except Exception as e:
        exceptionHandled = {"Exception": str(e)}
        return exceptionHandled


def getInstrumentByID(_id):
    try:
        query = {"_id": ObjectId(_id)}
        results = collectionInstrumentos().find_one(query)

        if results is None:
            return {"message": "No hay instrumento con ese _id!"}
        else:
            return results
    except Exception as e:
        exceptionHandled = {"Exception": str(e)}
        return exceptionHandled


def getInstrumentsByName(name):
    try:
        query = {"instrumento": {"$regex": name, "$options": "i"}}
        results = collectionInstrumentos().find(query)

        resultsList = list(results)

        if len(resultsList) == 0:
            return {"message": "No existen instrumentos que contengan la busqueda!"}
        else:
            return results
    except Exception as e:
        exceptionHandled = {"Exception": str(e)}
        return exceptionHandled


def newInstrument(instrumento):
    try:
        collectionInstrumentos().insert_one(instrumento)
        return instrumento
    except Exception as e:
        exceptionHandled = {"Exception": str(e)}
        return exceptionHandled


def updateName(_id, name):
    try:
        query = {"_id": ObjectId(_id)}
        set_name = {
            "$set": {
                "instrumento": name
            }
        }
        collectionInstrumentos().update_one(query, set_name)
        return {"message": "Nombre actualizado exitosamente!"}
    except Exception as e:
        exceptionHandled = {"Exception": str(e)}
        return exceptionHandled


def deleteInstrument(_id):
    try:
        query = {"_id": ObjectId(_id)}
        result = collectionInstrumentos().find_one_and_delete(query)
        if result is None:
            return {"message": "No existe instrumento con ese _id. Por lo tanto, no se pudo borrar."}
        else:
            return {"message": "Objeto borrado exitosamente!"}
    except Exception as e:
        exceptionHandled = {"Exception": str(e)}
        return exceptionHandled
