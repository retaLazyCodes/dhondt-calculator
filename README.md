## Python Fullstack Challenge

#### Tabla de contenidos

- [Requisitos funcionales](#Requisitos-funcionales)
- [Arquitectura del backend](#Arquitectura-del-backend)
- [Requisitos para ejecutar](#Requisitos-para-ejecutar)
- [Cómo ejecutar](#Cómo-ejecutar)


#### Requisitos funcionales

Objetivo: Implementar una API RESTful para calcular la distribución de escaños utilizando
el sistema D'Hondt.

Referencia: https://es.wikipedia.org/wiki/Sistema_D%27Hondt

**Requisitos:**
    1. El usuario debe poder ingresar a través de una solicitud a la API.
    2. El usuario debe poder ingresar la cantidad de escaños a disputarse.
    3. El usuario debe poder ingresar la cantidad de votos para cada una de las listas. Para simplificar, se puede fijar la cantidad de listas en 10, pero el sistema debe ser fácilmente escalable.
    4. El usuario debe poder ingresar las listas y la cantidad de votos asociados a cada una.
    5. El usuario debe poder consultar como quedó la distribución de escaños asignados a cada lista.
    6. El sistema debe almacenar y permitirle al usuario consultar el historial de cálculos realizados.

**Aclaraciones:**
    1. Desarrolla la API utilizando Python y un framework como Flask o FastAPI.
    2. Utiliza una base de datos para almacenar el historial de cálculos. Puedes utilizar SQLite, PostgreSQL, MySQL u otro.
    3. Documenta la API.
    4. El sistema debe poder ejecutarse de forma sencilla para verificar el correcto funcionamiento (por ejemplo, con el uso de Docker y Docker Compose).
    5. El usuario debe poder interactuar con el sistema a través de una interfaz gráfica. Para esto puedes usar el stack de tecnologías que creas necesario.
    6. Sigue las buenas prácticas de desarrollo, como el uso de control de versiones (Git), estructura de proyecto adecuada y manejo de errores.

#### Arquitectura del backend
Este proyecto sigue una arquitectura en capas que organiza el código en diferentes niveles de responsabilidad. La estructura se divide en las siguientes capas:

**1. Capa de Modelo**
    Descripción: Define las estructuras de datos y las reglas de negocio fundamentales.
    Responsabilidad: Representa las entidades y relaciones de la aplicación, así como la lógica de validación y transformación de datos.
**2. Capa de Repositorio**
    Descripción: Maneja la persistencia y recuperación de datos.
    Responsabilidad: Interactúa con la base de datos o cualquier otra fuente de datos. Se encarga de realizar operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y abstrae la lógica de acceso a datos de la aplicación.
**3. Capa de Controlador**
    Descripción: Contiene la lógica de negocio y de aplicación.
    Responsabilidad: Procesa las solicitudes recibidas, coordina la interacción entre los modelos y los repositorios, y gestiona la lógica de negocio. Actúa como intermediario entre la capa de API y la capa de modelo.
**4. Capa de API**
    Descripción: Expone los puntos finales de la aplicación para la interacción externa.
    Responsabilidad: Define los endpoints de la API y maneja las solicitudes HTTP. Traduce las peticiones del usuario en llamadas a la capa de controlador y devuelve las respuestas adecuadas.

#### Requisitos para ejecutar
Tener instalado:

- Docker Compose
- Git

#### Cómo ejecutar

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/retaLazyCodes/dhondt-calculator.git
```

Navega hasta el directorio del repositorio clonado:
```bash
cd dhondt-calculator
```

Por último ejecuta el siguiente comando para iniciar la aplicación con Docker Compose:
```bash
docker-compose up
```

Una vez que los contenedores estén en funcionamiento, puedes acceder al cliente de la aplicación ingresando a http://localhost:3000 en tu navegador web. 
También puedes acceder a la documentación de los endpoints de la API accediendo a http://localhost:8000/docs o http://localhost:8000/redoc.

