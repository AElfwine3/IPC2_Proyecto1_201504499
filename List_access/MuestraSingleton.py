from Use_cases import ListaMuestra

class MuestraSingleton:

    __instance = None

    @staticmethod
    def getInstance():
        if MuestraSingleton.__instance == None:
            MuestraSingleton()
        return MuestraSingleton.__instance
    
    def __init__(self):
        if MuestraSingleton.__instance != None:
            raise Exception("Ya existe una instancia!")
        else:
            self.listaMuestra = ListaMuestra.ListaMuestra()
            MuestraSingleton.__instance = self