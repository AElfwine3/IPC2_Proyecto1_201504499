import random

class Organismo:

    def __init__(self, codigo: str, nombre:str):
        self.codigo = codigo
        self.nombre = nombre
        self.color = self.asignar_color()
        self.siguiente = None
    
    def asignar_color(self):
        for i in range(3):
            r = random.randint(0,255)
            g = random.randint(0,255)
            b = random.randint(0,255)
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        return hex_color