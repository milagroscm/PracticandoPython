class Usuario:
    #metodos
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self):
        print('hola! mi nombre es ', self.nombre, self.apellido)
    
#creando una instancia tienen que ser 
#en minusculas
usuario = Usuario('felipe', 'feliz')
usuario2 = Usuario('chanchito', 'feliz')

#print(usuario.nombre, usuario.apellido, usuario2.nombre, usuario2.apellido)
usuario.saludo()
usuario2.saludo()