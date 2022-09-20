import services.instrumentosServices as instrumentServices
from flask import Response, request
from bson import json_util


def getAllInstruments():
    return Response(json_util.dumps(instrumentServices.getAllInstruments()), mimetype="application/json")


def getInstrumentByID(_id):
    return Response(json_util.dumps(instrumentServices.getInstrumentByID(_id)), mimetype="application/json")


def getInstrumentsByName(name):
    return Response(json_util.dumps(instrumentServices.getInstrumentsByName(name)), mimetype="application/json")


def newInstrument():
    newInstrumento = {
        "instrumento": request.json["instrumento"],
        "marca": request.json["marca"],
        "modelo": request.json["modelo"],
        "imagen": request.json["imagen"],
        "precio": request.json["precio"],
        "costoEnvio": request.json["costoEnvio"],
        "cantidadVendida": request.json["cantidadVendida"],
        "descripcion": request.json["descripcion"]
    }
    return Response(json_util.dumps(instrumentServices.newInstrument(newInstrumento)), mimetype="application/json")


def updateName():
    _id = request.json["_id"]
    name = request.json["instrumento"]
    return Response(json_util.dumps(instrumentServices.updateName(_id, name)), mimetype="application/json")


def deleteOneInstrumentByID(_id):
    return Response(json_util.dumps(instrumentServices.deleteOneInstrumentByID(_id)), mimetype="application/json")
