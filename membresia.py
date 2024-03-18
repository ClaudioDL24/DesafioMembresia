# Importando la clase abstracta ABC para definir una clase abstracta
from abc import ABC, abstractmethod

# Definición de la clase abstracta Membresia que no puede ser instanciada directamente
class Membresia(ABC): # Esta marcada como abstracta ya que hereda la clase ABC de python
    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):# Metodo Constructor para iniciaar los atributos de instancia de clase
        """Constructor de la clase Membresia.

        Args:
            correo_suscriptor (str): Correo del suscriptor.
            numero_tarjeta (str): Número de tarjeta del suscriptor.
        """
        self.__correo_suscriptor = correo_suscriptor
        self.__numero_tarjeta = numero_tarjeta

    @property #decorador de python 
    def correo_suscriptor(self): # Esto permitira acceder al atributo privado __correo_suscriptor
        return self.__correo_suscriptor

    @property
    def numero_tarjeta(self): # Esto permitira acceder al atributo privado __numero_tarjeta
        return self.__numero_tarjeta
    
    @abstractmethod #decorador de python que debe ser utilizado ya que la clase Membresia no puede ser instanciada directamente
    def cambiar_suscripcion(self, nueva_membresia: int):#Se define metodo abstracto cambiar_suscrpcion
        """Método abstracto para cambiar la suscripción de la membresía.

        Args:
            nueva_membresia (int): Nuevo tipo de membresía.
        """
        pass
     # Método privado para crear una nueva membresía
    def _crear_nueva_membresia(self, nueva_membresia: int):
        """Método privado para crear una nueva membresía.

        Args:
            nueva_membresia (int): Nuevo tipo de membresía.

        Returns:
            Membresia: Objeto de la nueva membresía.
        """
        if nueva_membresia == 1:
            return Basica(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 2:
            return Familiar(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 3:
            return SinConexion(self.correo_suscriptor, self.numero_tarjeta)
        elif nueva_membresia == 4:
            return Pro(self.correo_suscriptor, self.numero_tarjeta)

# Definición de la clase de membresía Gratis
class Gratis(Membresia): # hereda todas las propiedades y métodos de la clase Membresia.
    costo = 0
    cantidad_dispositivos = 1

    def cambiar_suscripcion(self, nueva_membresia: int):
        if nueva_membresia < 1 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

# Definición de la clase de membresía Básica
class Basica(Membresia): #Hereda la clase Membresia propiedades y metodos y agrega 2 atributos propios
    costo = 3000
    cantidad_dispositivos = 2

    def __init__(self, correo_suscriptor: str, numero_tarjeta: str):
        """Constructor de la clase Basica.

        Args:
            ccorreo_suscriptor (str): Correo del suscriptor.
            numero_tarjeta (str): Número de tarjeta del suscriptor.
        """
        super().__init__(correo_suscriptor, numero_tarjeta) # Llama al constructor de la clase base Membresia, inicializando el correo del suscriptor y el número de tarjeta con los valores proporcionados.

        if isinstance(self, Familiar) or isinstance(self, SinConexion): # Verifica si la instancia actual de la clase Basica es también una instancia de las clases Familiar o SinConexion
            self.__dias_regalo = 7

        elif isinstance(self, Pro):  #Verifica si la instancia actual de la clase Basica es también una instancia de la clase Pro.
            self.__dias_regalo = 15
    #Metodo para cancelar suscripción
    def cancelar_suscripcion(self):
        """Método para cancelar la suscripción de la membresía básica.

        Returns:
            Gratis: Objeto de membresía gratuita.
        """
        return Gratis(self.correo_suscriptor, self.numero_tarjeta)
    #Metodo para cambiar membresia
    def cambiar_suscripcion(self, nueva_membresia: int):
        """Método para cambiar la suscripción de la membresía básica.

        Args:
            nueva_membresia (int): Nuevo tipo de membresía.

        Returns:
            Membresia: Nueva membresía.
        """
        if nueva_membresia < 2 or nueva_membresia > 4:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

# Definición de la clase de membresía Familiar
class Familiar(Basica):
    costo = 5000
    cantidad_dispositivos = 5

    def cambiar_suscripcion(self, nueva_membresia: int):
        """Método para cambiar la suscripción de la membresía familiar.

        Args:
            nueva_membresia (int): Nuevo tipo de membresía.

        Returns:
            Membresia: Nueva membresía.
        """
        if nueva_membresia not in [1, 3, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)
    # Método para modificar el control parental
    def modificar_control_parental(self):
        pass


class SinConexion(Basica):
    costo = 3500

    def cambiar_suscripcion(self, nueva_membresia: int):
        """Método para cambiar la suscripción de la membresía sin conexión.

        Args:
            nueva_membresia (int): Nuevo tipo de membresía.

        Returns:
            Membresia: Nueva membresía.
        """
        if nueva_membresia not in [1, 2, 4]:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

    def incrementar_cantidad_maxima_offline(self):
        pass


class Pro(Familiar, SinConexion):
    costo = 7000
    cantidad_dispositivos = 6

    def cambiar_suscripcion(self, nueva_membresia: int):
        """Método para cambiar la suscripción de la membresía Pro.

        Args:
            nueva_membresia (int): Nuevo tipo de membresía.

        Returns:
            Membresia: Nueva membresía.
        """
        if nueva_membresia < 1 or nueva_membresia > 3:
            return self
        else:
            return self._crear_nueva_membresia(nueva_membresia)

# Creación de una membresía gratuita y prueba de cambio de membresía
g = Gratis("correo@prueba.cl", "123 456 789")
print(type(g))
b = g.cambiar_suscripcion(1)
print(type(b))
f = b.cambiar_suscripcion(2)
print(type(f))
sc = f.cambiar_suscripcion(3)
print(type(sc))
pro = sc.cambiar_suscripcion(4)
print(type(pro))
g2 = pro.cancelar_suscripcion()
print(type(g2))
