# Prueba-Zweicom
Prueba de Zweicom


## Desarrollo
El lenguaje utilizado es Python 2.7 con libreria Flask.
El objetivo es construir un servicio web que entregando un numero 'n' este retorne la posicion n y n-1 de la sucesion de Fibonacci, contando la primera posicion como la numero 0. La forma de entregar este numero es a travez de un JSON que lo contiene. 

### Prerrequisitos
Instalar pip para luego instalar la libreria Flask

```
$ sudo apt-get install python-pip
$ pip install flask
```
## Ejecucion
En terminal ir a la ubicacion donde esta el servicio dentro del computador, ejecutar con
```
$  python prueba_zweicom.py
```
y enviar un POST en formato JSON al url "0.0.0.0:5000/post" con el siguiente formato

```
{"n": (Aqui insertar numero correspondiente a la ubicacion de fibonacci que se quiere obtener)}
```
