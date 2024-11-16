from fastapi import APIRouter
import matplotlib.pyplot as plt
import io
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.get("/generate-chart")
def generate_chart():
    # Criar um gráfico simples
    plt.figure(figsize=(6, 4))
    plt.plot([1, 2, 3, 4], [10, 20, 25, 30], label="Sample Data")
    plt.title("Sample Line Chart")
    plt.legend()
    
    # Salvar o gráfico em memória
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return StreamingResponse(buf, media_type="image/png")
