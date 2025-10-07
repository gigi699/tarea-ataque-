# usuarios_lab.py

import uvicorn
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, EmailStr
from typing import Optional, List

app = FastAPI(title="Demo Laboratorio - Usuarios")

# -------------------------------
# Esquemas Pydantic
# -------------------------------
class LoginSchema(BaseModel):
    nombre: str
    clave: str

class UserCreateSchema(BaseModel):
    nombre: str
    clave: str
    correo: EmailStr
    activo: bool = True

class UserUpdateSchema(BaseModel):
    nombre: Optional[str] = None
    correo: Optional[EmailStr] = None
    activo: Optional[bool] = None

class UserOut(BaseModel):
    id: int
    nombre: str
    correo: EmailStr
    activo: bool

# -------------------------------
# "Base de datos" en memoria
# -------------------------------
DB_USUARIOS = {
    1: {"id": 1, "nombre": "admin", "clave": "abc", "correo": "admin@cipherwall.com", "activo": True},
    2: {"id": 2, "nombre": "user1", "clave": "secret", "correo": "user1@lab.com", "activo": True},
}
NEXT_ID = 3

# -------------------------------
# Funciones de utilidad
# -------------------------------
def obtener_por_id(uid: int):
    return DB_USUARIOS.get(uid)

def obtener_por_nombre(nombre: str):
    for u in DB_USUARIOS.values():
        if u["nombre"] == nombre:
            return u
    return None

# -------------------------------
# Endpoints
# -------------------------------
@app.get("/", summary="Página de inicio")
def home():
    return {"mensaje": "Bienvenido al Laboratorio de Seguridad - Demo"}

@app.post("/auth/login", summary="Iniciar sesión")
def login(datos: LoginSchema):
    usuario = obtener_por_nombre(datos.nombre)
    if not usuario or usuario["clave"] != datos.clave:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")
    if not usuario["activo"]:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Cuenta desactivada")
    return {"message": "login successful", "user": usuario["nombre"]}

@app.post("/usuarios", response_model=UserOut, status_code=status.HTTP_201_CREATED, summary="Crear usuario")
def crear_usuario(payload: UserCreateSchema):
    global NEXT_ID
    if obtener_por_nombre(payload.nombre):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nombre ya en uso")
    
    nuevo = {
        "id": NEXT_ID,
        "nombre": payload.nombre,
        "clave": payload.clave,
        "correo": payload.correo,
        "activo": payload.activo,
    }
    DB_USUARIOS[NEXT_ID] = nuevo
    NEXT_ID += 1
    return {"id": nuevo["id"], "nombre": nuevo["nombre"], "correo": nuevo["correo"], "activo": nuevo["activo"]}

@app.get("/usuarios", response_model=List[UserOut], summary="Listar todos los usuarios")
def listar_usuarios():
    return [
        {"id": u["id"], "nombre": u["nombre"], "correo": u["correo"], "activo": u["activo"]}
        for u in DB_USUARIOS.values()
    ]

@app.get("/usuarios/{uid}", response_model=UserOut, summary="Obtener usuario por id")
def obtener_usuario(uid: int):
    usuario = obtener_por_id(uid)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    return {"id": usuario["id"], "nombre": usuario["nombre"], "correo": usuario["correo"], "activo": usuario["activo"]}

@app.put("/usuarios/{uid}", summary="Actualizar usuario")
def actualizar_usuario(uid: int, cambios: UserUpdateSchema):
    usuario = obtener_por_id(uid)
    if not usuario:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    
    if cambios.nombre is not None:
        otro = obtener_por_nombre(cambios.nombre)
        if otro and otro["id"] != uid:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nombre ya en uso")
        usuario["nombre"] = cambios.nombre
    
    if cambios.correo is not None:
        usuario["correo"] = cambios.correo
    if cambios.activo is not None:
        usuario["activo"] = cambios.activo
    
    return {"mensaje": "Usuario actualizado", "usuario": {"id": usuario["id"], "nombre": usuario["nombre"], "correo": usuario["correo"], "activo": usuario["activo"]}}

@app.delete("/usuarios/{uid}", summary="Eliminar usuario")
def borrar_usuario(uid: int):
    if uid not in DB_USUARIOS:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")
    del DB_USUARIOS[uid]
    return {"mensaje": f"Usuario {uid} eliminado"}

# -------------------------------
# Ejecutar con: python usuarios_lab.py
# o con: python -m uvicorn usuarios_lab:app --reload
# -------------------------------
if __name__ == "__main__":
    uvicorn.run("usuarios_lab:app", host="127.0.0.1", port=8000, reload=True)
