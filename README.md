# Prueba-Zweicom
Prueba de Zweicom


## Desarrollo
El lenguaje utilizado es Python 2.7 con libreria Flask

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
