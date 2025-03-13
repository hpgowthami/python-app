from celery import Celery
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from src.db.models import QRCodeMetadata
from src.db.session import get_db_session

app = Celery('worker', broker='redis://localhost:6379/0')

@app.task
def clean_expired_qr_codes():
    db: Session = get_db_session()
    expiration_time = datetime.utcnow() - timedelta(days=30)
    expired_qr_codes = db.query(QRCodeMetadata).filter(QRCodeMetadata.created_at < expiration_time).all()
    
    for qr_code in expired_qr_codes:
        db.delete(qr_code)
    
    db.commit()