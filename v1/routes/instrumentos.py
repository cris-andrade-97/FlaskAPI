from flask import Blueprint, jsonify, request
import controllers.instrumentosController as controller

instrumentos_bp = Blueprint("route-instrumentos", __name__, url_prefix="/api/instrumentos")


@instrumentos_bp.route("/", methods=["GET"])
def getAllInstruments():
    results = controller.getAllInstruments()
    if "Exception" in results.json:
        return error500(results.json["Exception"])
    else:
        return results


@instrumentos_bp.route("/<_id>", methods=["GET"])
def getInstrumentByID(_id):
    results = controller.getInstrumentByID(_id)
    if "Exception" in results.json:
        return error500(results.json["Exception"])
    else:
        return results


@instrumentos_bp.route("/busqueda/<name>", methods=["GET"])
def getInstrumentByName(name):
    results = controller.getInstrumentsByName(name)
    if "Exception" in results.json:
        return error500(results.json["Exception"])
    else:
        return results


@instrumentos_bp.route("/", methods=["POST"])
def newInstrument():
    results = controller.newInstrument()
    if "Exception" in results.json:
        return error500(results.json["Exception"])
    else:
        return results


@instrumentos_bp.route("/", methods=["PATCH"])
def updateNameOfOneInstrument():
    results = controller.updateName()
    if "Exception" in results.json:
        return error500(results.json["Exception"])
    else:
        return results


@instrumentos_bp.route("/<_id>", methods=["DELETE"])
def deleteInstrumentByID(_id):
    results = controller.deleteOneInstrumentByID(_id)
    if "Exception" in results.json:
        return error500(results.json["Exception"])
    else:
        return results


@instrumentos_bp.errorhandler(404)
def error404(error=None):
    response = jsonify({
        "message": "¡Esa dirección no existe!: " + request.url,
        "status": 404
    })
    response.status_code = 404

    return response


@instrumentos_bp.errorhandler(500)
def error500(error=None):
    response = jsonify({
        "message": "Internal Server Error: " + error,
        "status": 500
    })
    response.status_code = 500

    return response
