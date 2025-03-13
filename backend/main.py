from fastapi import FastAPI
from config.db import engine, Base
from api.routesUser import routerUser
from api.routesAddress import routerAddress
from api.routesCategory import routerCategory
from api.routesProduct import routerProduct
from api.routesOrder import routerOrder
from api.routesPayMethod import routerPayMethod
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
Base.metadata.create_all(bind=engine)
# Registrar rutas

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # ✅ Permite Angular
    allow_credentials=True,
    allow_methods=["*"],  # ✅ Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # ✅ Permite todos los headers
)

app.include_router(routerPayMethod)
app.include_router(routerProduct)
app.include_router(routerCategory)
app.include_router(routerUser)
app.include_router(routerAddress)
app.include_router(routerOrder)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)