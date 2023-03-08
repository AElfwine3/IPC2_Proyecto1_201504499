from Use_cases import ListaOrganismo

class OrganismoSingleton:

    __instance = None

    @staticmethod
    def getInstance():
        if OrganismoSingleton.__instance == None:
            OrganismoSingleton()
        return OrganismoSingleton.__instance
    
    def __init__(self):
        if OrganismoSingleton.__instance != None:
            raise Exception("Ya existe una instancia!")
        else:
            self.listaOrganismo = ListaOrganismo.ListaOrganismo()
            OrganismoSingleton.__instance = self