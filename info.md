# Generar cuentas de servicio y enviarlas a un grupo de google.

⚫ Puedes encontrar el tutorial completo en  [UNIQedumx](https://uniq.edu.mx/generar-cuentas-de-servicio-google-console-y-agregarlas-al-grupo-google/) - [Aqui el video](https://github.com/smartass08/telegram_gcloner)
- [x] Manual para Replit, Linux y Windows
- [x] Crear cuentas de servicio
- [x] Renombrar cuentas de servicio a numeros.
- [x] Agregar cuentas de servicio a grupo google para usuario gmail de 10 en 10.
- [x] Agregar cuentas de servicio a grupo google para usuario Gsuite administrador de 100 en 100.
- [x] Agregar cuentas de servicio a team drive


## Proceso para realizarlo en Replit
_Tener una cuenta en replit_

#### 1. Ir a [Replit](https://replit.com/) acceder
- New repl e importar con github
- Pega el siguiente repositorio

```
https://github.com/abdiasriver/CuentasGooglegroups
```

- Si te pregunta que tipo de proyecto selecciona python

#### 2. Instala los requerimientos

`pip install -r requirements.txt`

#### 3. Nuevo proyecto en console de google.
- Abre [console de google](https://console.cloud.google.com)  y crea un nuevo proyecto
- Ve a Pantalla de consentimiento de OAuth, selecciona **externo** y un nombre a tu app.
- Crea credenciales de tipo **ID de clientes OAuth**
- Descarga las credenciales con nombre **credentials.json** 
- Sube **credentials.json** a replit

#### 4. Generar cuentas de servcio
_Podemos generar 100,200,300..600..,cuentas de servicio con credentials_

- Crear token y Autorizar

`python3 gentoken.py`

_Dale click al link y autoriza,despues copia y pega el codigo en la consola y dale enter_

- Listar proyectos creados en google console ,el primero en la lista es el creado mas reciente.

`python3 gen.py --list-projects`

- Crear proyecto **extra** al creado desde google console cambia el 1 por los que quieras, cada proyecto soporta 100 cuentas de servicio.

`python3 gen.py --create-projects 1`

_Si creas un proyecto o mas recuerda volver a listar para que tengas los ID de los proyectos ya que los utilizaras_

#### 5. Activar los servicios **iam** y **Drive** con el siguiente comando, para cada proyecto

`python3 gen.py --enable-services ID-del-proyecto`

#### 6. Crear las cuentas de servicio para cada uno de los proyectos creados

`python3 gen.py --create-sas ID-del-proyecto`


#### 7. Descargar las cuentas de servicio a la carpeta **accounts**, repite este proceso para cada uno de los proyectos que vayas a usar

`python3 gen.py --download-keys ID-del-proyecto`

**Nota** Ahora si quieres eliminar las claves de un proyecto, haz lo siguiente (solo se eliminaran las claves en el proyecto no en la carpeta accounts)
#### 8. Eliminar las claves en un proyecto, este es un comando extra, por si quieres reutilizar proyectos creados y quieras eliminar sus claves, o cambiarlas.

`python3 gen.py --delete-sas ID-del-proyecto`


#### 9. Renombrar las cuentas de servicio a numeros por ejemplo a 0.json 1.json etc.

- Ir a la carpeta accounts y renombrar los archivos
```
cd accounts
python3 rename.py
```
- Regresar a la carpeta principal
`cd ..`

#### 10. Agregar cuentas de servicio a grupo google para usuario gmail de 10 en 10.
- Imprimir las cuentas en grupo de 10 en 10 para agregarlas a un grupo de google.

`python3 emails.py`

_Despues de ello copialos de 10 en 10 y ve agregandolos al grupo de google, recuerda que solo permite agregar 100 cuentas por dia_
- Agrega ese grupo a tu Team Drive o a carpetas que te van a compartir.

#### 11. Descargar los archivos en zip 

`zip -r uniqedumxbot.zip *`

#### 11. Agregar cuentas de servicio a grupo google para usuario Gsuite administrador de 100 en 100.
_Para realizar esto tienes que ser administrador de Gsuite_

- Activa en el proyecto creado en google console la Biblioteca de API **Admin SDK**
- Tienes que tener un grupo de google
- Separa los .json de 100 en 100 , puedes usar carpetas fuera de accounts y meter 100, despues quitarlos a otra carpeta y poner los otros 100
_El problema es que el script no manda todos de un jalon y quedan cuentas sin enviar, por eso de 100 en 100 mejor_
- Lanza el siguiente script y concede los permisos

`python3 add_to_google_group.py -g usuariodegrupo@udominio.com`

- Agrega ese grupo a tu Team Drive o a carpetas que te van a compartir.


## Para sistemas Linux
**Para sistemas Linux**: Instalar pyhton
- Instala python-pip ,screen,git dependiendo tu distribucion yo usare archlinux
`yay -S python-pip screen git`

- Clona este repositorio con git

```
git clone https://github.com/abdiasriver/CuentasGooglegroups.git
cd CuentasGooglegroups
```
- Sigue los pasos 2 hasta el 11 o el que necesitas.

## Para sistemas Windows

- Instala [Python](https://www.python.org/downloads/)
- Descarga este repositorio y descomprimelo
- Abre un **cmd** y ve la direccion de la carpeta

```
cd CuentasGooglegroups
```

- Instala los requerimientos puede ser **pip** o **pip3** y para usar python pueden ser **py** o **python3**

`pip3 install -r requirements.txt`

- Sigue los pasos 2 hasta el 11 o el que necesitas.
- Puedes visitarnos en telegram @cinedriveonline



