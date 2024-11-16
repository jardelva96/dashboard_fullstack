from sqlalchemy.orm import Session
from app.models import ChartData

def get_all_data(db: Session):
    return db.query(ChartData).all()

def create_data(db: Session, label: str, value: float):
    data = ChartData(label=label, value=value)
    db.add(data)
    db.commit()
    db.refresh(data)
    return data
