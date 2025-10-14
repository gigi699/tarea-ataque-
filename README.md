# tarea-ataque-
Crear el entorno virtual
python -m venv venv (si no te genera errores puedes probar usando "py" en lugar de "python", Por qué da error? Ni idea, pero así me funciono)

Activar en Windows
.\venv\Scripts\activate

Activar en macOS/Linux
source venv/bin/activate

Instala las dependencias. Utiliza el archivo requirements.txt para instalar todas las librerías necesarias.

pip install -r requirements.txt

Ejecución de la API Una vez configurado el entorno, puedes iniciar el servidor de la API.
Abre una terminal en la raíz del proyecto.

Ejecuta el siguiente comando:

uvicorn main:app --reload

O también puedes usar:

fastapi dev

El servidor estará activo en http://127.0.0.1:8000.

Puedes acceder a la documentación interactiva de la API (generada por Swagger UI) en http://127.0.0.1:8000/docs.

Análisis de Seguridad y Demostración de Vulnerabilidad Esta API tiene un endpoint /login que es vulnerable a ataques de fuerza bruta. Esto se debe a dos razones principales:
No hay límite de intentos (Rate Limiting): Un atacante puede intentar iniciar sesión miles de veces sin ser bloqueado.

No hay bloqueo de cuentas: Una cuenta puede ser objeto de infinitos intentos fallidos sin que se bloquee temporalmente.

Cómo Demostrar la Vulnerabilidad El script Brute_force.py está diseñado para simular este ataque en nuestro entorno local y controlado.

Asegúrate de que el servidor de la API se esté ejecutando (paso anterior).

Abre una segunda terminal.

Ejecuta el script de ataque, especificando el nombre de usuario que quieres vulnerar. La API tiene dos usuarios por defecto: admin (contraseña: "admin") y Dario (contraseña: "abc").

Intenta encontrar la contraseña del usuario "admin"
python Brute_force.py admin

Observarás en la terminal del atacante cómo se prueban contraseñas de forma incremental hasta encontrar la correcta. Al mismo tiempo, en la terminal del servidor API, verás el flujo de peticiones POST /login entrantes.
