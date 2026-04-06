"""Cree una clase de Python llamada Usuario que use el método init y cree un nombre de usuario 
y una contraseña. Crea un objeto usando la clase."""

class Usuario:
    #Método constructor llamado al crear un objeto. 
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

    def  formato(self):
        return f'Usuario: {self.nombre}\n Contraseña: {self.contrasena}'



usuario1 = Usuario('camilo', 'papalote')
print(usuario1.formato())
