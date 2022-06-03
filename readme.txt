

Introducción

Un cliente nos plantea la necesidad de inventariar la información de los cablemodems que tiene en su
red, para ello nos solicita desarrollar una herramienta que le permita determinar obtener información
de un cablemodem a partir de su IP.
Adicionalmente se le suma la problemática de que no toda la información de los cablemodems los
tienen que tener en el mismo medio de almacenamiento, ya que hay algunos de estos tienen que ser
importados en un sistema que solo soporta importación de archivos, y otros en un sistema que
soporta la importación por base de datos. Se puede dar que la información de un cablemodem tenga
que ser importada en ambos sistemas.
Por esta razón se solicita desarrollar una aplicación que dada una determinada dirección IP de un
cablemodem, se obtenga vía SNMP la información de fabricante, modelo y versión de software. Los
cuales se deben almacenar en el destino dado.
Los parámetros que se ingresarán en la aplicación serán los siguientes:
● ip: Dirección IP del cablemodem.
● destination: Donde se almacenará la información, esta puede ser:
○ db: Se debe almacenar el fabricante, modelo y la versión de software en la base de
datos
○ file: Se debe almacenar el fabricante, modelo y versión de software en el file.
○ both: Se debe almacenar fabricante, modelo y versión de software en la base de datos
y archivo.
Condiciones solicitadas
La aplicación se ejecutará por CLI, por lo que se solicita que la IP y destino se puedan pasar como
argumentos de la aplicación (Ver ejemplos más adelante).
En caso de que un fabricante, modelo y versión de software ya esté almacenado en uno de los medios
se tiene que mostrar por pantalla el error.

Validaciones a considerar

● Se tiene que validar que la ip respete el formato IPv4
● Que el fabricante, modelo y versión de software no estén repetido en el mismo medio. En
caso de utilizar destination en “both” se debería validar en ambos medios.
● El CM puede no existir en la ip dada.
● Como comunidad SNMP se asume "private" para todos los CM.
Requerimientos no funcionales
● Se debe utilizar Python 3.4 o superior como lenguaje para desarrollar la aplicación.
● Se asume que todos los cablemodem soportan SNMP v2c
● Se debe utilizar mysql o mariadb como motor relacional.
● Se pueden utilizar todas las librerías que considere necesarias sin restricciones.

Ejemplos de input y output
input
python miApp.py 10.0.0.10 db
out
Se debe almacenar la información de vendor, modelo y versión de software en la base de datos.
input
python miApp.py 10.0.0.10 file
out
Se debe almacenar la información de vendor, modelo y versión de software en un file.
input
python miApp.py 10.0.0.11 file
out
Se debe almacenar la información de vendor, modelo y versión de software en un file.
input
python miApp.py 10.0.0.11 file
out
Debe tirar error porque ya existe la información de ese CM.
input
python miApp.py 10.0.0.11 both
out
Se debe tirar error porque ya está almacenado en file.
input
python miApp.py 10.0.0.11 db
out
Se debe almacenar la información de vendor, modelo y versión de software en la base de datos. Como
solo se almacenan en la base de datos, está ok.


Datos adicionales

La OID SNMP sugerida para consultar los datos del cablemodem es:
Name: sysDescr
OID: 1.3.6.1.2.1.1.1
IP de cablemodem de prueba: X.X.X.X
snmpget -v2c -c private X.X.X.X 1.3.6.1.2.1.1.1.0
iso.3.6.1.2.1.1.1.0 = STRING: "FAST3890V2 Wireless Voice Gateway <<HW_REV: V1.0; VENDOR: SAGEMCOM; BOOTR: 2.7.0alpha4;
SW_REV: FAST3890V2_SSC_US_50.7.6.T1; MODEL: FAST3890V2>>"


La tabla se tiene que llamar cm_models y tiene que tener la siguientes estructura:

● vendor: VARCHAR
● model: VARCHAR
● softversion: VARCHAR

Y el formato del archivo tiene que ser xml, como por ejemplo

<cm_models>
	<cm_model>
		<vendor></vendor>
		<model></model>
		<softversion></softversion>
	</cm_model>
.
.
.
	<cm_model>
		<vendor></vendor>
		<model></model>
		<softversion></softversion>
	</cm_model>
</cm_models>

