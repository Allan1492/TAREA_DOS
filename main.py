from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Lista para almacenar los usuarios
users = []

# Validar los datos del usuario
class User(BaseModel):
    name: str
    email: str

# **********************POST para crear un usuario******************************************************
@app.post("/users/")
def create_user(user: User):
    users.append(user.dict())  # Guardar usuario como diccionario
    return {"message": f"User {user.name} added successfully!", "user": user}