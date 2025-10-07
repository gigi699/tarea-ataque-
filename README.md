# tarea-ataque-
PS C:\Users\ortizb\Desktop> cd .\seguridad\
PS C:\Users\ortizb\Desktop\seguridad> ls


    Directorio: C:\Users\ortizb\Desktop\seguridad


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         7/10/2025     11:13                venv
d-----         7/10/2025     11:15                __pycache__
-a----         7/10/2025      8:05           2415 attack.py
-a----         11/6/2025     15:23           4558 codigo funcional royecto.txt
-a----         7/10/2025      8:35           4920 usuarios_lab.py


PS C:\Users\ortizb\Desktop\seguridad> py attack.py
Introduce el nombre de usuario a atacar: admin
[*] Iniciando ataque de fuerza bruta contra el usuario: 'admin'
[+] Probando... (Intento #1000, Contraseña actual: '01')
1️⃣ Crear el entorno virtual

En la carpeta de tu proyecto (C:\Users\ortizb\Desktop\seguridad) abre la terminal y ejecuta:

python -m venv venv


Esto creará una carpeta llamada venv dentro de tu proyecto con Python aislado.

2️⃣ Activar el entorno virtual

En Windows (CMD):

venv\Scripts\activate


Si usas PowerShell:

venv\Scripts\Activate.ps1


Si la activación funciona, verás (venv) al inicio de la línea de comandos.

3️⃣ Instalar los paquetes necesarios

Con el entorno activado, instala FastAPI, Uvicorn y email-validator:

pip install fastapi uvicorn "pydantic[email]"


Esto asegura que tengas todo lo que tu proyecto necesita.

4️⃣ Ejecutar tu API

Con el entorno activo, corre:

python -m uvicorn usuarios_lab:app --reload


Ahora debería correr sin conflictos de importación.

💡 Tip: Cada vez que cierres la terminal y quieras trabajar en el proyecto, solo activa el entorno con:

venv\Scripts\activate
uvicorn main:app --reload --host 127.0.0.1 --port 8000
La API estará en http://127.0.0.1:8000.
Abre el navegador en:
