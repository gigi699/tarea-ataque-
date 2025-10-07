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
uvicorn main:app --reload --host 127.0.0.1 --port 8000
La API estará en http://127.0.0.1:8000.
Abre el navegador en:
