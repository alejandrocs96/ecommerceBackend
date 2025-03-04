from fastapi import FastAPI
from config.db import engine, Base
from api.routesUser import routerUser
from api.routesAddress import routerAddress
from api.routesCategory import routerCategory
from api.routesProduct import routerProduct
app = FastAPI()
Base.metadata.create_all(bind=engine)
# Registrar rutas

app.include_router(routerProduct)
app.include_router(routerCategory)
app.include_router(routerUser)
app.include_router(routerAddress)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)