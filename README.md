# Desafío Guiado: Membresía

Este proyecto es un desafío que contempla crear una estructura de clases que permita crear membresías de usuarios suscriptores.

## Descripción

Has sido contratado como programador/a backend por una empresa que se encuentra
desarrollando una aplicación de streaming de videos de películas y series chilenas. En esta
ocasión, se te ha solicitado desarrollar la estructura de clases que permita crear membresías
de los usuarios suscriptores. Existen 5 tipos de membresía: Gratis, Básica, Familiar, Sin
Conexión y Pro.
Como el foco actual es el diseño, solo se le ha pedido considerar que para crear cada
membresía se debe solicitar el correo electrónico y el número de tarjeta (como texto) del
suscriptor. Adicionalmente, algunos tipos de membresía reciben días de regalo al crearse
(reciben un valor fijo, pero que en el futuro podría se decidir modificar). En cuanto a las
funcionalidades, todos los tipos de membresía deben permitir cambiar la suscripción, lo que
genera una nueva membresía (según el tipo solicitado) conservando el correo electrónico y el
número de tarjeta de la membresía original.
Para el cambio de membresía, debe utilizar un identificador numérico para identificar el tipo
de membresía solicitada, según lo siguiente:
○ 1: Básica
○ 2: Familiar
○ 3: Sin Conexión
○ 4: Pro
NOTA: Puedes utilizar el método “_crear_nueva_membresia” (dentro de la(s)
clase(s) que estimes adecuado) que se encuentra en el archivo
apoyo_desafio.py. Este método tiene un nivel de acceso de tipo “protected”
(dado por el underscore “_” al principio del nombre). Un método de tipo “protected”
solo puede ser accedido por la misma clase donde se define, y por
 todas las clases que le hereden.
_ 2
www.desafiolatam.com
En cuanto al detalle de los tipos de membresía, debes tener en cuenta las siguientes
consideraciones para el desarrollo solicitado:
● No puede existir una “Membresía” como tal, sino que siempre debe ser de algún tipo
específico, que se detalla en los siguientes puntos.
● Todas las membresías de tipo “Gratis” tienen un costo de $0, y una cantidad máxima
de 1 dispositivo. Comportamiento:
○ Si alguien con este tipo de membresía desea cambiar su suscripción, debe
validar que la nueva membresía solicitada sea un número entre 1 y 4 inclusive,
y luego generar la nueva membresía. En caso contrario, debe retornar la
membresía actual.
● Todas las membresías de tipo “Básica” tienen un costo de $3000, y una cantidad
máxima de 2 dispositivos. Comportamiento:
○ Si alguien con este tipo de membresía desea cambiar su suscripción, debe
validar que la nueva membresía solicitada sea un número entre 2 y 4 inclusive,
y luego generar la nueva membresía. En caso contrario, debe retornar la
membresía actual.
● Todas las membresías de tipo “Familiar” tienen un costo de $5000, y una cantidad
máxima de 5 dispositivos. Al momento de crear una membresía Familiar, se debe
asignar 7 a un atributo de instancia que almacene los días de regalo. Comportamiento:
○ Si alguien con este tipo de membresía desea cambiar su suscripción, debe
validar que la nueva membresía solicitada sea un 1, 3 ó 4, y luego generar la
nueva membresía. En caso contrario, debe retornar la membresía actual.
○ Debe permitir modificar el control parental. La lógica de este comportamiento
aún no se ha definido, pero debe declararlo (sin implementación).
● Todas las membresías de tipo “Sin Conexión” tienen un costo de $3500, y una cantidad
máxima de 2 dispositivos. Al momento de crear una membresía Sin Conexión, se debe
asignar 7 a un atributo de instancia que almacene los días de regalo. Comportamiento:
○ Si alguien con este tipo de membresía desea cambiar su suscripción, debe
validar que la nueva membresía solicitada sea un 1, 2 ó 4 , y luego generar la
nueva membresía. En caso contrario, debe retornar la membresía actual.
○ Debe permitir incrementar la cantidad máxima de contenido disponible para
ver sin conexión. La lógica de este comportamiento aún no se ha definido, pero
debe declararlo (sin implementación).
● Todas las membresías de tipo “Pro” tienen un costo de $7000, y una cantidad máxima
de 6 dispositivos. Al momento de crear una membresía Pro, se debe asignar 15 a un
atributo de instancia que almacene los días de regalo. Comportamiento:
_ 3
www.desafiolatam.com
○ Si alguien con este tipo de membresía desea cambiar su suscripción, debe
validar que la nueva membresía solicitada sea un número entre 1 y 3 inclusive,
y luego generar la nueva membresía. En caso contrario, debe retornar la
membresía actual.
○ Debe permitir modificar el control parental (igual a membresía Familiar)
○ Debe permitir incrementar la cantidad máxima de contenido disponible para
ver sin conexión (Igual a membresía Sin Conexión).
● Las membresías de tipo “Básica”, “Familiar”, “Sin Conexión” y “Familiar” deben tener
además el siguiente comportamiento:
○ Deben permitir cancelar la suscripción. Al realizar esta acción, se debe generar
una membresía de tipo Gratis con el mismo correo y número de tarjeta de la
membresía original.
Tips:
● Para resolver este desafío con menos líneas de código, puede aplicar herencia híbrida,
donde:
○ Dos de las clases son padre de más de una clase (herencia jerárquica).
○ Tres de las clases son hija y padre a la vez (herencia multinivel).
○ Una de las clases hereda de más de una clase (herencia múltiple).
● Considerando lo anterior, el ordenamiento de las clases puede ser el siguiente:

## Empezando 🚀

Estas instrucciones te guiarán para obtener una copia de este proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

Clonar el repositorio

```bash
git clone urlgit
```

### Prerrequisitos 📋

Lista de software y herramientas, incluyendo versiones, que necesitas para instalar y ejecutar este proyecto:

- Sistema Operativo (por ejemplo, Ubuntu 20.04, Windows 10)
- Lenguaje de programación (por ejemplo, Python 3.8)
- Framework (por ejemplo, Django 3.1)
- Base de datos (por ejemplo, PostgreSQL 12)
- Otros...
