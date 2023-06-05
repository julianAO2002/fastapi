from fastapi import FastAPI
from routers import jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()


# Rutas: "/jwt_auth_user", "/users_db", 
app.include_router(jwt_auth_users.router)
app.include_router(users_db.router)
app.mount("/static", StaticFiles(directory="static"), name="static")



@app.get("/")
async def root():
    return "Hola mundo desde FastAPI!"




@app.get("/url")
async def url():
    return {"url": "repositorio"}

# Inicia el server: uvicorn main:app --reload
# Url local: http://127.0.0.1:8000/url

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc
