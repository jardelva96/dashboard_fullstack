from fastapi import FastAPI
from app.routers import charts
from app.database import engine
from app.models import Base

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend do Dashboard está funcionando!"}

app.include_router(charts.router)
