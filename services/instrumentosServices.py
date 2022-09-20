import database.models.InstrumentoDAO as modelInstrumento


def getAllInstruments():
    return modelInstrumento.getAllInstruments()


def getInstrumentByID(_id):
    return modelInstrumento.getInstrumentByID(_id)


def getInstrumentsByName(name):
    return modelInstrumento.getInstrumentsByName(name)


def newInstrument(instrumento):
    return modelInstrumento.newInstrument(instrumento)


def updateName(_id, name):
    return modelInstrumento.updateName(_id, name)


def deleteOneInstrumentByID(_id):
    return modelInstrumento.deleteInstrument(_id)
