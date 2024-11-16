from fastapi import FastAPI
from app.routers import charts
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Rota inicial
@app.get("/")
def read_root():
    return {"message": "Dashboard Backend is Running"}

# Incluir rotas do arquivo charts
app.include_router(charts.router)

# Adicionar uma nova rota no arquivo principal
@app.get("/export")
def export_data():
    # Lógica para geração de relatório
    return {"message": "Export endpoint is under construction"}
