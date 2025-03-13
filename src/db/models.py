from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class QRCodeMetadata(Base):
    __tablename__ = 'qr_code_metadata'

    id = Column(Integer, primary_key=True, index=True)
    data = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    expires_at = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<QRCodeMetadata(id={self.id}, data={self.data}, created_at={self.created_at}, expires_at={self.expires_at})>"