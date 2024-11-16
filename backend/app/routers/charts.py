from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import ChartData

router = APIRouter()

@router.get("/data")
def read_chart_data(db: Session = Depends(get_db)):
    return db.query(ChartData).all()

@router.post("/data")
def create_chart_data(label: str, value: float, db: Session = Depends(get_db)):
    new_data = ChartData(label=label, value=value)
    db.add(new_data)
    db.commit()
    db.refresh(new_data)
    return {"message": "Dados adicionados com sucesso", "data": new_data}
